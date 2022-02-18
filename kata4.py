


from ntpath import join

text= """Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

# Divide el texto
divide = text.split('. ')
print(divide)
# Palabras clave
clave = ["average", "temperature", "distance"]
# Ciclo for para recorrer la cadena
for text2 in divide:
    for palabra in clave:
        if palabra in text2:
            print(text2)
            break
# Ciclo para cambiar C a Celsius
for text2 in divide:
    for palabra in clave:
        if palabra in text2:
            print(text2.replace(' C', ' Celsius'))
            break

# Datos con los que vas a trabajar
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"

titulo = "Datos de gravedad sobre " + planet
print(titulo.title())

gravedad = gravity * 1000

datos = "Gravedad en " + name + '\n' "es " + str(gravedad) + '\n' "Nombre del planeta: " + planet
print(datos)

# Unión de ambas cadenas
union = titulo.title() + "\n" + join(datos)

print(union)

# Nuevos datos muestra
planeta = 'Marte '
gravedad1  = 0.00143
nombre = 'Ganímedes'

# Comprobamos la plantilla
print(datos)

#Nueva plantilla
datos2 = "Gravedad en " + nombre + '\n' "es " + str(gravedad1) + '\n' "Nombre del planeta: " + planeta
print(datos2.format(nombre=nombre, planeta=planeta, gravedad1=gravedad1))
 
# Pista: print(nueva_plantilla.format(variables))
print(datos2.format(nombre=nombre, planeta=planeta, gravedad1=(gravedad1*1000)))
