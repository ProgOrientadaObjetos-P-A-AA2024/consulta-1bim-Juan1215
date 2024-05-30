class Jugador():
    
    def __init__(self, nombre, dorsal):
        self.nombre = nombre
        self.dorsal = dorsal

    def Jugador(self):
        print(self.nombre, "tiene el dorsal", self.dorsal)

jugador1 = Jugador("Leonel Messi", 10)
jugador1.Jugador()

jugador2 = Jugador("Crstiano Ronaldo", 7)
jugador2.Jugador()

