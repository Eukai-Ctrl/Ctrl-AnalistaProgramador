import pyqrcode
from PIL import Image #PIL es una biblioec de pthon (Python Imaging Library)

def generar_codigo_qr(dato):
    
    qr_code = pyqrcode.create(dato) #Genera el qr
    
    
    qr_code.png(f"{dato}.png", scale=8) #Guarada qr como imagen

def ingresar_datos():
    datos = {}
    datos_ingresados = 0
    
    while datos_ingresados < 10:
        print(f"Ingresando datos ({datos_ingresados + 1}/10):") #muestra el numero de datos ingresados como contador 
        isbn = input("ISBN: ")
        pais_codigo = input("PAIS código: ")
        identificador = input("Identificador Publicador/Editorial: ")
        folio = input("Folio de la Edición: ")
        titulo_libro = input("Nuevo título del libro: ")
        autor_libro = input("Nuevo nombre del autor: ")
        cantidad_paginas = input("Nuevo cantidad de páginas: ")
        fecha_publicacion = input("Nuevo fecha de la primera publicación: ")
        
        # Almacenar los datos en el diccionario
        datos[isbn] = {
            "PAIS código": pais_codigo,
            "Identificador": identificador,
            "Folio de la Edición": folio,
            "Nuevo título del libro": titulo_libro,
            "Nuevo nombre del autor": autor_libro,
            "Nuevo cantidad de páginas": cantidad_paginas,
            "Nuevo fecha de la primera publicación": fecha_publicacion
        }
        
        
        for valor in datos.values(): #genera un qr para cada dato
            for dato in valor.values():
                generar_codigo_qr(dato)
        
        datos_ingresados += 1
        
    return datos # devuelve diccionario datos el que contiene toda la info 

if __name__ == "__main__": # llama a la funsion ingrese datos y ejecuta 
    datos = ingresar_datos()
    print("Datos ingresados:", datos)
