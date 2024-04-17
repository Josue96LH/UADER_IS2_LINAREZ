# ------------------------------------------------------------------------------------------------------------------
# Trabajo Practico N° 3 - Patrones de Creacion.
# Josue Linarez Hein
# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
# Punto 5:
# Extienda el ejemplo visto en el taller en clase de forma que se pueda utilizar
# para construir aviones en lugar de vehículos. Para simplificar suponga que un
# avión tiene un “body”, 2 turbinas, 2 alas y un tren de aterrizaje.
# ------------------------------------------------------------------------------------------------------------------

"""En este caso use el programa IS2_taller_car.py"""

import os


class Director:
    """Clase que orquesta la construcción del avión."""

    def setBuilder(self, builder):
        """Asigna un constructor específico al director."""
        self.__builder = builder

    def getAirplane(self):
        """Construye un avión utilizando el constructor asignado."""
        airplane = Airplane()

        # Construcción del avión: body, turbinas, alas y tren de aterrizaje
        body = self.__builder.getBody()
        airplane.setBody(body)

        for _ in range(2):
            engine = self.__builder.getEngine()
            airplane.attachEngine(engine)

        for _ in range(2):
            wing = self.__builder.getWing()
            airplane.attachWing(wing)

        landing_gear = self.__builder.getLandingGear()
        airplane.setLandingGear(landing_gear)

        return airplane


class Airplane:
    """Clase que representa un avión."""

    def __init__(self):
        self.__engines = list()
        self.__wings = list()
        self.__body = None
        self.__landing_gear = None

    def setBody(self, body):
        """Establece el cuerpo del avión."""
        self.__body = body

    def attachEngine(self, engine):
        """Añade un motor al avión."""
        self.__engines.append(engine)

    def attachWing(self, wing):
        """Añade un ala al avión."""
        self.__wings.append(wing)

    def setLandingGear(self, landing_gear):
        """Establece el tren de aterrizaje del avión."""
        self.__landing_gear = landing_gear

    def specification(self):
        """Imprime las especificaciones del avión."""
        print("Cuerpo: %s" % (self.__body.shape))
        print("Número de turbinas: %d" % (len(self.__engines)))
        print("Número de alas: %d" % (len(self.__wings)))
        print("Tipo de tren de aterrizaje: %s" % (self.__landing_gear.type))


class Builder:
    """Clase base para el constructor de aviones."""

    def getEngine(self): pass
    def getWing(self): pass
    def getBody(self): pass
    def getLandingGear(self): pass


class AirplaneBuilder(Builder):
    """Constructor específico para construir aviones."""

    def getEngine(self):
        """Crea y devuelve un motor."""
        engine = Engine()
        # Se pueden definir los detalles del motor aquí
        return engine

    def getWing(self):
        """Crea y devuelve un ala."""
        wing = Wing()
        # Se pueden definir los detalles del ala aquí
        return wing

    def getBody(self):
        """Crea y devuelve el cuerpo del avión."""
        body = Body()
        # Se pueden definir los detalles del cuerpo aquí
        return body

    def getLandingGear(self):
        """Crea y devuelve el tren de aterrizaje del avión."""
        landing_gear = LandingGear()
        # Se pueden definir los detalles del tren de aterrizaje aquí
        return landing_gear


class Engine:
    """Clase que representa un motor de avión."""
    # Se pueden agregar más atributos según sea necesario
    pass


class Wing:
    """Clase que representa un ala de avión."""
    # Se pueden agregar más atributos según sea necesario
    pass


class Body:
    """Clase que representa el cuerpo de un avión."""
    # Se pueden agregar más atributos según sea necesario
    pass


class LandingGear:
    """Clase que representa el tren de aterrizaje de un avión."""
    # Se pueden agregar más atributos según sea necesario
    pass


def main():
    """Función principal del programa."""
    airplane_builder = AirplaneBuilder()
    director = Director()
    director.setBuilder(airplane_builder)
    airplane = director.getAirplane()

    airplane.specification()
    print("\n\n")


if __name__ == "__main__":
    os.system("clear")
    print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un avión\n")

    main()
