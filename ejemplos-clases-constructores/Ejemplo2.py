class Constructores2():

    def __init__(self, nombre, caarrera, ciclo):
        self.nombre = nombre
        self.carrera = caarrera
        self.cliclo = ciclo
    def informacion(self):
        return "{} esta en la carrarera de {} y esta cursando {}".format(self.nombre, self.carrera, self.cliclo)
       
persona1 = Constructores2("Juan Villamagua", "Computacion", "Segundo ciclo")
print(persona1.informacion())

persona2 = Constructores2("Diego Alvarado", "Computacion", "Sexto ciclo")
print(persona2.informacion())