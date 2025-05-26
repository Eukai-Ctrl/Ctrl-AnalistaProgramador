class Estudiante:
    def __init__(self,nombre,grado):
        self.nombre = nombre
        self.grado = grado
    def presentarse(self):
        print("Hola soy ",self.nombre,"y estoy en el ",self.grado,"grado.")
        #print(f"Hola soy {self.nombre} y estoy en el {self.grado} grado.")
        
