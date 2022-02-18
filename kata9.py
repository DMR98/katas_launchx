# Función para leer 3 tanques de combustible y muestre el promedio

def Tanques(Gasolina, Gas, Oxigeno):
    Promedio = (Gasolina + Gas + Oxigeno) / 3
    return f"""Reporte:
    Promedio: {Promedio}%
    Gasolina: {Gasolina}%
    Gas: {Gas}%
    Oxigeno: {Oxigeno}% 
    """

# Llamamos a la función que genera el reporte print(funcion(tanque1, tanque2, tanque3))

print(Tanques(50, 80, 75))


# Función promedio 
def Promedio(values):
    total = sum(values)
    numero = len(values)
    return total / numero

Promedio([80, 85, 81]) 

# Actualiza la función
def Tanques(Gasolina, Gas, Oxigeno):
    return f"""Reporte:
    Promedio : {Promedio([Gasolina, Gas, Oxigeno])}%
    Gasolina : {Gasolina}%
    Gas: {Gas}%
    Oxigeno: {Oxigeno}% """

print(Tanques(55, 90, 85))

#EJERCICIO 2
# Función con un informe preciso de la misión. Considera hora de prelanzamiento, tiempo de vuelo, destino, tanque externo y tanque interno

def Reporte_mision(hora_lanzamiento, timepo_vuelo, destino, tanque_externo, tanque_interno):
    return f"""
    Mision a {destino}
    Total hora de viaje: {hora_lanzamiento + timepo_vuelo} minutos
    Total de conbustible: {tanque_externo + tanque_interno} galones
    """

print(Reporte_mision(30, 41, "Luna", 200000, 300000))