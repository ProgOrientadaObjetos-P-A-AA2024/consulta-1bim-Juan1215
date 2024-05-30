
miLista = ["Juan", "Pedro", "Jose", "Miguel"]
edades = ["12", "14" , "12", "13"]
promedios = [9.5, 8, 5.5, 6]
print(miLista)
print(edades)
print(promedios)

print("=============")

miLista.append("Carlos")
print(miLista)

edades.insert(5, "15")
print(edades)

promedios.append(7.9)
print(promedios)

print("=============")

sumaPromedios = sum(promedios)
promedios = len(promedios)
promedio = sumaPromedios / promedios
print(f"Suma de los promedios: {promedio}")
