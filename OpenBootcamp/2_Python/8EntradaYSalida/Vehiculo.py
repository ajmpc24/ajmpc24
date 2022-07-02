import pickle


class Vehiculo():
   
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

cocheNuevo1 = Coche("violeta", 4, 4, 100, 8)
f = open("datos.bin", "rb")
coche = pickle.load(f)
f.close()

print(type(coche))
print(cocheNuevo1.color)
print(cocheNuevo1.ruedas)
print(cocheNuevo1.puertas)
print(cocheNuevo1.velocidad)
print(cocheNuevo1.cilindrada)

