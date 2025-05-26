
import math


class Figura:
    
    def  calcular_area(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
    @classmethod
    def crear_circulo(cls,radio):
        class Circulo(Figura):
            
            def __init__(self,radio):
                self.radio = radio
                
            def calcular_area(self):
                return math.pi * (self.radio **2)
            
        return Circulo(radio)
    @classmethod
    def crear_rectangulo(cls,ancho,alto):
        class Rectangulo(Figura):
            def __init__(self,ancho,alto):
                self.ancho = ancho
                self.alto = alto
            
            def calcular_area(self):
                return self.ancho * self.alto
            
        return Rectangulo(ancho,alto)
    
    @classmethod
    def crear_triangulo(cls,base,altura):
        class Triangulo(Figura):
            def __init__(self,base,altura):
                self.base = base
                self.altura = altura
                
            def calcular_area(self):
                return (self.base*self.altura)/2
        return Triangulo(base,altura)
                
    
    
            
    