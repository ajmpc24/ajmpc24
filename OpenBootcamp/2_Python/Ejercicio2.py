#Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.

#Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]
listaDeNumeros = [1,2,3,4,5,6,7,8,9,10]
listaDeNumerosImpar = []

for i in listaDeNumeros:
    resultado = i % 2
    if resultado != 0:
        listaDeNumerosImpar.append(i)
        print(listaDeNumerosImpar)