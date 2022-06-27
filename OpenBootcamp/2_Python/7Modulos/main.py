# Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas.
# Los resultados tenéis que mostrarlos por consola.
import calculadora


def main():
    resultado = calculadora.suma(4, 6)
    print("El resultado de las suma es:", resultado)

    resultado = calculadora.resta(4, 6)
    print("El resultado de las resta es:", resultado)

    resultado = calculadora.multiplicacion(4, 6)
    print("El resultado de las multiplicacion es:", resultado)

    resultado = calculadora.division(4, 6)
    print("El resultado de las division es:", resultado)

if __name__ == '__main__':
    main()
