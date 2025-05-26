from instancia_figuras import Figura

class appFiguras:
    def ejecutar (self):
        
        #crear un circulo con radio 5
        circulo = Figura.crear_circulo(5)
        print (f"El area del circulo con radio 5 es: {circulo.calcular_area():.2f}")
        
        
        #Crear un rectangulo con ancho  4 y alto 6 
        rectagulo = Figura.crear_rectangulo(4,6)
        print (f"El area del rectangulo con ancho 4 y alto 6 es:{rectagulo.calcular_area()}")
        
        #Crear un Triangulo equilatero de base 5 y altura 4.33
        triangulo = Figura.crear_triangulo(5,4.33)
        print(f"El area de un triangulo con base 5 y altura 4.33 es :{triangulo.calcular_area():.2f}")
        
        
        
if __name__ == "__main__":
    app = appFiguras()
    app.ejecutar()
    
    