# Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.
import math

def areaTriangulo(base, altura):
    resultado = base * altura / 2
    print("El area de un triangulo es: ")
    print(resultado)
areaTriangulo(6, 22)


def areaCirculo(radio):
    resultado = math.pi * radio * radio
    print("El area de un circulo es: ")
    print(resultado)
areaCirculo(5)