class Alumno: #Creamos la clase
    Nombre = ''     #Añadimos nuestro atributos
    Materia = ''
     
    def print_information(self, Nombre, Materia): #Definimos nuetro metodo
        print (self.Nombre) 
        print (self.Materia)
             
Daniel = Alumno() #Creamos nuestro objeto de la clase Alumno
Daniel.Nombre = 'Daniel'   #Completamos los atributos creados
Daniel.Materia = 'Español'
Daniel.print_information(Daniel.Nombre, Daniel.Materia) #Vamos al metodo para imprimir
