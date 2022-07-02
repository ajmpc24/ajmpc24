# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y
# escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

#Crean archivo  de texto .txt
f = open("datos.txt","w")
#escribindo dentro del archivo
f.write("Crean do anrchivo .txt para ejercicio 1 del modulo 8 del tema entrada y salida del curso de python\n")
#cerrando dentro del archivo
f.close()

#Abriendo archivo .txt
f = open("datos.txt","a")
f.write("Archivo creado e ingresando nuevos dato.")
f.close()