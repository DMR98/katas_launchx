# Declara dos variables

planets = []

new_planet = input('Ingresa un Planeta ')

# Escribe el ciclo while solicitado
while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
        print(planets)
        break


# Escribe tu ciclo for para iterar en una lista de planetas

for planet in planets:
    print(planet)
    break