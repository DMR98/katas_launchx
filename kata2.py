#Mostrar fecha
from datetime import date
print("Toda's date is: " + str(date.today()))

#Convertidor de unidades
parsec = 11

lightyears = 3.26156

conversion = (parsec * lightyears)

print(str(parsec) + " parsec, is " + str(lightyears) + " lightyears")
print("El total de " + str(parsec) + " parsec es de " + str(conversion) + " años luz" )