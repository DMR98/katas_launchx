# Añadir el código necesario para crear una variable que guarde la velocidad del asteroide.
velocidad = 49

# Escribe una expresión de prueba para calcular si necesita una advertencia.
if velocidad < 25:
    print("ADVERTENCIA, un asteroide se acerca rapidamente")
# Agregue las instrucciones que se ejecutarán si la expresión de prueba es true o false.
else:
    print("Todo se encuentra bien por hoy")

# Agrega el código para crear una variable para un asteroide que viaja a 19 km/s
velocidad2 = 19
# Escribe varias expresiones de prueba para determinar si puedes ver el rayo de luz desde la tierra
if velocidad2 <= 19:
    print("Atentos se vera un destello en el cielo")
# Agrega las instrucciones que se ejecutarán si las expresiones de prueba son True o False
else:
    print("Todo por hoy se encuentra bien")


# Agrega el código para crear nuevas variables para la velocidad y el tamaño del asteroide
# Para probar el código, prueba con varias velocidades y tamaños
# Escribe varias expresiones de prueba o combinaciones de expresiones de prueba para determinar qué mensaje se debe enviar a Tierra.
velocidad3 = 25
tamano = 40
if velocidad3 > 25 and tamano > 25:
    print('¡ADVERTENCIA, Un asteroide se acerca a la tierra')
elif velocidad3>= 20:
    print('Miren el cielo, un destello de luz se visualizará')
elif tamano < 25:
    print('Todo bien por hoy')
else:
    print('Tu día será excelente')