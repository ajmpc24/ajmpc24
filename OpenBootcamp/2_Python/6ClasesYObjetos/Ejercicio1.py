# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
class Vehiculo():
   
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
class Coche(Vehiculo):

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.
cocheNuevo1 = Coche("violeta", 4, 4, 100, 8)
print("El coche nuevo es de color: ")
print(cocheNuevo1.color)
print("tiene la cantidad de ruedas: ")
print(cocheNuevo1.ruedas)
print("tiene la cantidad de puertas: ")
print(cocheNuevo1.puertas)
print("tiene una cilindrada de: ")
print(cocheNuevo1.cilindrada)