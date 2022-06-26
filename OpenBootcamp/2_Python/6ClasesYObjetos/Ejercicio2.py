
class Alumno:

    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
 
    def imprimir(self):
               print("Nombre: ",self.nombre)
               print("Nota: ",self.nota)
 
    def aprobo(self):
            if self.nota >= 6:
                print("Aprobado!!!")
            else:
                print("Reprobado!!")
 

alumnoNuevo = Alumno()

alumnoNuevo.inicializar("Vitaly",8)
alumnoNuevo.imprimir()
alumnoNuevo.aprobo()

alumnoNuevo = Alumno()

alumnoNuevo.inicializar("Jose",5)
alumnoNuevo.imprimir()
alumnoNuevo.aprobo()