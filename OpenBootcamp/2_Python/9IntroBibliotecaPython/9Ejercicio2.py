# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares
# de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos
# obtenidos mediante reduce.


listaDeNumeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


def numeroImpares(numero):
    if numero % 2 != 0:
        return True

    return False


resultado = filter(numeroImpares, listaDeNumeros)
print(list(resultado))
