class Calculadora:
    
    def __init__(self,valor1,valor2):
        self.valor1 = valor1
        self.valor2 = valor2
        
    def suma(self):
        return  self.valor1 + self.valor2
    
    def restar(self):
        return self.valor1 - self.valor2
    
    def multiplicar(self):
        return self.valor1 * self.valor2
    
    def dividir(self):
        if self.valor2 != 0 :  # lo hacemos de esta manera para evitar la divisiones por 0 
            return self.valor1 / self.valor2 
        else:
            return "Error:Division por 0 no permitida"
        
        #  agregar  3 funciones , raiz cuadrada  , potencia , porcentaje 
        
        
        #return self.valor1 / self.valor2
    
    
    
    
    