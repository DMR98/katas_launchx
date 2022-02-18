# Crea un diccionario llamado planet con los datos propuestos
planet = {
    'name': 'Mars',
    'moons': 2
}

print(planet)
# Muestra el nombre del planeta y el número de lunas que tiene.
print(planet.get('name'))
print(planet.get('moons'))

# Agrega la clave circunferencia con los datos proporcionados previamente
planet['circunferencia(km)'] = {
    'polar': 6752,
    'equatorial': 6792
}

print(planet)

# Imprime el nombre del planeta con su circunferencia polar.
print(f'Planeta:  {planet["name"]} tiene como circunferencia polar: {planet["circunferencia(km)"]["polar"]}')

# Planets and moons  EJERCICIO 2

planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

# Añade el código para determinar el número de lunas.
lunas = planet_moons.values()
planetas = len(planet_moons.keys())

# Agrega el código para contar el número de lunas. 

total_lunas = 0
for moon in lunas:
    total_lunas = total_lunas + moon

promedio = total_lunas / planetas

print("El promedio de lunas es de ", promedio)

