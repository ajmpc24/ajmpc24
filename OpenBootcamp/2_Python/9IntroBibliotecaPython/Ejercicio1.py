# Crea un script que le pida al usuario una lista de países (separados por comas).
# Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set).
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.
listasDePaises = []


def listasDePaises():
    pais = input("Ingrese un pais: ")
    listasDePaises = []
    while pais != "end":
        if pais not in listasDePaises:
            listasDePaises.append(pais)
        pais = input('Ingrese el nombre del pais o "end" para cerrar: ')

    return listasDePaises


print()
print()
print("Los paises son: ", listasDePaises())
