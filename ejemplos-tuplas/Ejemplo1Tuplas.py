
# Las tuplas son practicamente los mismo que una lista 
# pero con la diferencia que en las tuplas no se pueden modificar 
miTupla = ("Juan", "Pedro", "Jose", "Miguel")
print(miTupla)

print(miTupla[2])

#Me dice la posicion de donde esta lo que ingrese
print(miTupla.index("Juan"))

# Esto nos permite combiar de tuplas a una lista 
# donde esto me va a permitir realizar funciones que tiene una lista
miTupla = list(miTupla)
print(type(miTupla))

miTupla.append("Julian")
print(miTupla)

