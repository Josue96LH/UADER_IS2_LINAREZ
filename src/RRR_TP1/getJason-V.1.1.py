# Copyright UADERFCyT-IS2©2024 Todos los derechos reservados.

import json
import sys
import argparse
from abc import ABC, abstractmethod

class JSONKeyRetrieverInterface(ABC):
    """
    Interfaz para definir el comportamiento de los recuperadores de claves JSON.
    """
    @abstractmethod
    def get_value(self):
        """
        Método abstracto para obtener el valor de una clave.
        """
        pass

class OriginalJSONKeyRetriever(JSONKeyRetrieverInterface):
    """
    Implementación original del recuperador de claves JSON.
    """
    def __init__(self, jsonfile, jsonkey='token1'):
        self.jsonfile = jsonfile
        self.jsonkey = jsonkey

    def get_value(self):
        """
        Recupera el valor de la clave especificada en el archivo JSON.
        """
        try:
            with open(self.jsonfile, "r") as myfile:
                data = myfile.read()
            obj = json.loads(data)
        except FileNotFoundError:
            self._print_error(f"El archivo '{self.jsonfile}' no existe.")
        except json.JSONDecodeError:
            self._print_error(f"El archivo '{self.jsonfile}' no contiene un JSON válido.")
        
        if self.jsonkey in obj:
            return str(obj[self.jsonkey])
        else:
            self._print_error(f"La clave '{self.jsonkey}' no existe en el archivo JSON.")
    
    def _print_error(self, message):
        """
        Muestra un mensaje de error y termina el programa.
        """
        print(f"Error: {message}")
        sys.exit(1)

class RefactoredJSONKeyRetriever(JSONKeyRetrieverInterface):
    """
    Implementación refactorizada del recuperador de claves JSON.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(RefactoredJSONKeyRetriever, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, jsonfile=None, jsonkey='token1'):
        if self._initialized:
            return
        self.jsonfile = jsonfile
        self.jsonkey = jsonkey
        self.data = self.read_json_file()
        self._initialized = True

    def read_json_file(self):
        """
        Lee el archivo JSON y lo convierte en un objeto Python.
        """
        try:
            with open(self.jsonfile, "r") as myfile:
                data = myfile.read()
            return json.loads(data)
        except FileNotFoundError:
            self._print_error(f"El archivo '{self.jsonfile}' no existe.")
        except json.JSONDecodeError:
            self._print_error(f"El archivo '{self.jsonfile}' no contiene un JSON válido.")

    def get_value(self):
        """
        Recupera el valor de la clave especificada en el archivo JSON.
        """
        if not self.data:
            self._print_error("No se pudo leer el contenido del archivo JSON.")
        if self.jsonkey in self.data:
            return str(self.data[self.jsonkey])
        else:
            self._print_error(f"La clave '{self.jsonkey}' no existe en el archivo JSON.")

    def _print_error(self, message):
        """
        Muestra un mensaje de error y termina el programa.
        """
        print(f"Error: {message}")
        sys.exit(1)

class JSONKeyRetrieverContext:
    """
    Contexto para manejar los recuperadores de claves JSON.
    """
    def __init__(self, retriever: JSONKeyRetrieverInterface):
        self.retriever = retriever

    def get_value(self):
        """
        Obtiene el valor de la clave utilizando el recuperador especificado.
        """
        return self.retriever.get_value()

def main():
    """
    Función principal del programa.
    """
    # Configurar el analizador de argumentos
    parser = argparse.ArgumentParser(description="Recuperar el valor de una clave en un archivo JSON.")
    parser.add_argument('jsonfile', type=str, help='Ruta del archivo JSON')
    parser.add_argument('jsonkey', type=str, nargs='?', default='token1', help='Clave a recuperar (por defecto: token1)')
    parser.add_argument('--refactored', action='store_true', help='Usar la implementación refactorizada')
    parser.add_argument('-v', '--version', action='version', version='Versión 1.1')  # Agregar opción de versión
    
    # Parsear los argumentos
    args = parser.parse_args()

    # Validar los argumentos
    if not args.jsonfile.endswith('.json'):
        print("Error: El archivo debe tener una extensión .json")
        sys.exit(1)
    
    # Seleccionar la implementación
    if args.refactored:
        retriever = RefactoredJSONKeyRetriever(args.jsonfile, args.jsonkey)
    else:
        retriever = OriginalJSONKeyRetriever(args.jsonfile, args.jsonkey)
    
    # Crear el contexto
    context = JSONKeyRetrieverContext(retriever)
    
    # Recuperar el valor y mostrarlo
    value = context.get_value()
    print(value)

if __name__ == "__main__":
    main()
