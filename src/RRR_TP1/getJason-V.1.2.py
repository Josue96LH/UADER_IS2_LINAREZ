# Copyright UADERFCyT-IS2©2024 Todos los derechos reservados.

import json
import sys
import argparse
from abc import ABC, abstractmethod
from datetime import datetime

class JSONKeyRetrieverInterface(ABC):
    """
    Interfaz para definir el comportamiento de los recuperadores de claves JSON.
    """
    @abstractmethod
    def get_value(self, token):
        """
        Método abstracto para obtener el valor de una clave dado un token.
        """
        pass

class JSONKeyRetriever:
    """
    Singleton que recupera la clave asociada a un token desde un archivo JSON.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(JSONKeyRetriever, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self.data = self.read_json_file()
        self._initialized = True

    def read_json_file(self):
        """
        Lee el archivo JSON y lo convierte en un objeto Python.
        """
        try:
            with open("sitedata.json", "r") as myfile:
                data = myfile.read()
            return json.loads(data)
        except FileNotFoundError:
            self._print_error("El archivo 'sitedata.json' no existe.")
        except json.JSONDecodeError:
            self._print_error("El archivo 'sitedata.json' no contiene un JSON válido.")

    def get_value(self, token):
        """
        Recupera el valor de la clave asociada a un token.
        """
        if not self.data:
            self._print_error("No se pudo leer el contenido del archivo JSON.")
        if token in self.data:
            return str(self.data[token])
        else:
            self._print_error(f"El token '{token}' no existe en el archivo JSON.")

    def _print_error(self, message):
        """
        Muestra un mensaje de error y termina el programa.
        """
        print(f"Error: {message}")
        sys.exit(1)

class BankAccount:
    """
    Clase para representar una cuenta bancaria.
    """
    def __init__(self, token, initial_balance=1000):
        self.token = token
        self.balance = initial_balance
        self.payments = []

    def make_payment(self, amount, order_number):
        """
        Realiza un pago desde la cuenta bancaria.
        """
        if self.balance >= amount:
            self.balance -= amount
            self.payments.append((order_number, amount, self.token))
            print(f"Pago de ${amount} realizado desde la cuenta '{self.token}'. Saldo restante: ${self.balance}")
        else:
            print(f"No hay saldo suficiente en la cuenta '{self.token}' para realizar el pago.")

    def list_payments(self):
        """
        Devuelve un iterador para listar todos los pagos realizados por orden cronológico.
        """
        return iter(sorted(self.payments, key=lambda x: x[0]))

class Command:
    """
    Interfaz para definir un comando.
    """
    @abstractmethod
    def execute(self):
        """
        Método abstracto para ejecutar el comando.
        """
        pass

class PaymentCommand(Command):
    """
    Comando para realizar un pago desde una cuenta bancaria.
    """
    def __init__(self, account, amount, order_number):
        self.account = account
        self.amount = amount
        self.order_number = order_number

    def execute(self):
        """
        Ejecuta el comando para realizar el pago.
        """
        self.account.make_payment(self.amount, self.order_number)

class CommandChain:
    """
    Cadena de comandos para controlar las cuentas bancarias.
    """
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        """
        Agrega un comando a la cadena.
        """
        self.commands.append(command)

    def execute_commands(self):
        """
        Ejecuta todos los comandos en la cadena.
        """
        for command in self.commands:
            command.execute()

def main():
    """
    Función principal del programa.
    """
    # Configurar el analizador de argumentos
    parser = argparse.ArgumentParser(description="Realizar pagos desde cuentas bancarias.")
    parser.add_argument('token', type=str, help='Token del banco (token1 o token2)')
    parser.add_argument('amount', type=float, help='Monto del pago')
    parser.add_argument('order_number', type=int, help='Número de pedido')
    parser.add_argument('-v', action='version', version='Versión 1.2')  # Avanzar a la versión 1.2
    
    # Parsear los argumentos
    args = parser.parse_args()

    # Validar el token del banco
    if args.token not in ['token1', 'token2']:
        print("Error: El token del banco debe ser 'token1' o 'token2'.")
        sys.exit(1)

    # Crear el recuperador de claves JSON
    key_retriever = JSONKeyRetriever()

    # Obtener la clave asociada al token del banco
    key = key_retriever.get_value(args.token)

    # Crear la cuenta bancaria
    bank_account = BankAccount(args.token)

    # Realizar el pago utilizando la cadena de comandos
    payment_command = PaymentCommand(bank_account, args.amount, args.order_number)
    command_chain = CommandChain()
    command_chain.add_command(payment_command)
    command_chain.execute_commands()

    # Listar todos los pagos realizados
    print("Listado de pagos realizados:")
    for order_number, amount, token in bank_account.list_payments():
        print(f"Número de pedido: {order_number}, Monto: ${amount}, Token: {token}")

if __name__ == "__main__":
    main()

    