# Creamos la lista planets y la mostramos
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planets)
# Agregamos a plutón y mostramos el último elemento
planets.append('Pluton')
print(planets)

# Ejercicio 2
# Lista de planetas


Planeta = input('Ingresa el nombre de un Planeta ')
 
Buscar = planets.index(Planeta)
# Muestra los planetas más cercanos al Planeta
print('Los planetas mas cerca de ' + Planeta)
print(planets[0:Buscar])

# Muestra los planetas más lejanos al Planeta

print('Los planetas mas lejos de ' + Planeta)
print(planets[Buscar + 1:])

