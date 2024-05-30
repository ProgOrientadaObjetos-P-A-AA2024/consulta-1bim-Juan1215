class Tienda():
    
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

persona1 = Tienda("Maria", "Viveres")
persona2 = Tienda("Jose", "Productos de limpiesa") 

print( "Hola", persona1.nombre, "\nQue productos compro:" , persona1.productos )
print( "Hola", persona2.nombre, "\nQue productos compro:" , persona2.productos )