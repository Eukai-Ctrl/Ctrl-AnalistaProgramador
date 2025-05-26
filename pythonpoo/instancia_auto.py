class Auto:
    def __init__ (self,Marca,Modelo):
        self.__Marca = Marca
        self.__Modelo = Modelo
        self.__Encendido = False
    
    def Arrancar (self):
        self.__Encendido = True
        print("El auto esta Encendido")
        print(self.__Encendido)
    
    def Detener (self):
        self.__Encendido = False
        print("El auto esta Apagado")
        print(self.__Encendido)
        