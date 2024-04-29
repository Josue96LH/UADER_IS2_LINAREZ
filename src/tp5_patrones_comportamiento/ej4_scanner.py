import os


class State:
    """Clase base para los estados de la radio."""
    def scan(self):
        """Simula el escaneo de estaciones de radio."""
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))


class AmState(State):
    """Clase que representa el estado de sintonización de AM."""
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        """Cambia el estado de la radio a FM."""
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate


class FmState(State):
    """Clase que representa el estado de sintonización de FM."""
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        """Cambia el estado de la radio a AM."""
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate


class Radio:
    """Clase que representa una radio con estados de sintonización."""
    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate
        self.am_memories = {"M1": "1250", "M2": "1380", "M3": "1510"}  # Frecuencias AM memorizadas
        self.fm_memories = {"M1": "81.3", "M2": "89.1", "M3": "103.9"}  # Frecuencias FM memorizadas

    def toggle_amfm(self):
        """Cambia entre los estados de sintonización de AM y FM."""
        self.state.toggle_amfm()

    def scan(self):
        """Escanea las estaciones y sintoniza las frecuencias memorizadas."""
        self.state.scan()
        if isinstance(self.state, AmState):
            print("Sintonizando frecuencias memorizadas AM:")
            for memory, frequency in self.am_memories.items():
                print("Sintonizando... Estación {} {}".format(frequency, memory))
        elif isinstance(self.state, FmState):
            print("Sintonizando frecuencias memorizadas FM:")
            for memory, frequency in self.fm_memories.items():
                print("Sintonizando... Estación {} {}".format(frequency, memory))


if __name__ == "__main__":
    os.system("clear")
    print("\nCrea un objeto radio y almacena las siguientes acciones")
    radio = Radio()
    actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
    actions *= 2

    print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
    for action in actions:
        action()
