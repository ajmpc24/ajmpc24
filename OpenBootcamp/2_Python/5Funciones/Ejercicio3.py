# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def anoBisiesto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        print("Es bisiesto")
    else:
        print("No es bisiesto")

anoBisiesto(1960)
anoBisiesto(1989)
anoBisiesto(1998)
anoBisiesto(2010)
anoBisiesto(2024)