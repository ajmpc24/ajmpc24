# Escribe una función que pueda decirte si un número (número entero) es primo o no.

def es_primo(numero):
  if numero<2:
    primo=False
  for i in range(2, numero):
     if  (numero % i)== 0:
        primo=False
     else:
        primo=True
  return primo

print(es_primo(4))