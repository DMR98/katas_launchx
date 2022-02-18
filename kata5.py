# Crear variables para almacenar las dos distancias
# ¡Asegúrate de quitar las comas!
from math import ceil, floor

distancia_tierra = 149597870
distancia_jupiter = 778547200

distancia = distancia_jupiter - distancia_tierra
kilometros = ceil(distancia * .0621)
print(distancia, kilometros)

# Almacenar las entradas del usuario
#Pista: variable = input("¿Cuál es tu nombre?")

planeta1 = input('Distancia del Planeta 1')
planeta2 = input('Distancia del Planeta 2')


planeta1 = int(planeta1)
planeta2 = int(planeta2)

distancia = planeta1 - planeta2

print(distancia)

distancia_km = distancia * 0.621
print(abs(distancia))



