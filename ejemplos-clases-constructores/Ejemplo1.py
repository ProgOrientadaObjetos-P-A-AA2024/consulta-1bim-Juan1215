class Constructores():
   
    def __init__(self, nombre, capacidad, años):
        self.nombre = nombre
        self.capacidad = capacidad
        self.años = años
    
    def informacion(self):
        print(f"Nombre de su local: {self.nombre}")
        print(f"Capacidad de personas: {self.capacidad}")
        print(f"Años en funcinamiento: {self.años} años")
       
local = Constructores("Raquelita", "200", 10)
local.informacion()