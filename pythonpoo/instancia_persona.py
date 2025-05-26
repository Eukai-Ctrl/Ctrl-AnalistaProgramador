# la ventaja de trabajar POO es que podemos modularizar el codigo, este es un modulo de un codigo mas grande  separado por OBJETO
#contructor vacio o con parametros. 
#con parametros, neecesita los datos para contruir la clase

class Persona:
    
    def __init__(self, edad, peso, altura, nombre):
        self.edad = edad 
        self.peso = peso
        self.altura = altura
        self.nombre = nombre
    
    def mostrar(self):
        print(f"Nombre:{self.nombre}") # f es una palabra reservada para que podeamos juntar un string con una variable que ente caso es "nombre"  y self.nombre
        print(f"Edad:{self.edad}")
        print(f"Altura:{self.altura}")
        print(f"Peso:{self.peso}")
    
    def mayor(self):
        return self.edad >= 18
    
        