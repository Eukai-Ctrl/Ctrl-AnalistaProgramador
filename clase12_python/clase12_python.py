#####################TRABAJO_3_PROGRAMACION##########################
import qrcode
from PIL import Image
isbn_libro = str("El ISBN de este libro es: ")
pais_codigo = str("El codigo del pais es: ")
identificador_editorial = str("El identificador es :")
folio_edicion = str ("El numero de folio es: ")
titulo_libro = str ("El titulo del libro es: ")
Nombre_autor = str ("El nombre del autor es: ")
cantidad_paginas = str("La cantidad de paginas es: ")
primera_publica = str ("La fecha de la primera publicacion es: ")
web_site = str ("El website del libro es: ")
print("######################################################################################################################")
print("######################################################################################################################")
print("######################################################################################################################")
print("################################# CREADOR DE QR BIBLIOTECA DE LOS OLVIDONES ##########################################")
print("######################################################################################################################")
print("######################################################################################################################")
print("######################################################################################################################")
print("################################ DESARROLLADO POR EL GRUPO --LOS OLVIDONES -- ########################################")
print("######################################################################################################################")
print("######################################################################################################################")
print("######################################################################################################################")
answer = int(8)
validador = int(8)
diccionario = int()
while answer == validador:
    print("INTRUCCIONES: ")
    print(              " 1. INGRESAR LOS DATOS SOLICITADOS,EN CASO DE NO TENERLOS DISPONIBLES INGRESAR -DESCONOCIDO- ")
    print(              " 2. VOLVER AL MENU PRINCIPAL UTILIZANDO EL NUMERO 8 Y SELECCIONE OPC 2 PARA CREACION DEL QR")
    print(              " 3. EN EL CASO DE ERROR DE INGRESO DE DATOS, REPETIR EL PROCESO VOLVIENDO AL MENU PRINCIPAL CON TECLA 8 Y LUEGO OPC 1")
    
    print("Opcion 1 : -	Agregar un libro y crear su QR")
    print("Opcion 2 : -	Crear QR de un libro ingresado anteriomente")
    opc = int (input("Ingrese numero de la  opcion seleccionada: "))
    if opc == 1:
      print("OPCION 1")
      mi_diccionario = {
            isbn_libro:str(input("Favor ingresar ISBN de libro: ")),
            pais_codigo:str(input("Favor ingresar PAIS de libro: ")),
            identificador_editorial:str(input("Favor ingresar identificador de la editorial: ")),
            folio_edicion:str(input("Favor ingresar folio de edicion del libro: ")),
            titulo_libro:str(input("Favor ingresar titulo del libro: ")),
            Nombre_autor:str(input("Favor ingresar nombre del autor: ")),
            cantidad_paginas:str(input("Favor ingresar cantidad paginas del libro: ")),
            primera_publica:str(input("Favor ingresar fecha de la primera publicacion del libro: ")),
            web_site:str(input("Favor ingrese el website del libro: "))
            }
      img = qrcode.make(mi_diccionario)
      type(img)  # qrcode.image.pil.PilImage2
      img.save(r'/Users/sebastiansalgado/Desktop/Seba/PROGRAMACION-nonube/qrlibros/QR-Libro-actual.jpg')
      i=int(input("Favor ingrese el N° de indentificacion del libro ingresado")) 
      mi_diccionario == diccionario 
      diccionario = diccionario + i
      
      
      answer = int (input ( "Si desea volver al menu principal marque 8  y si desea cerrar el INGRESO de libros marque 9: ")) 
    elif opc == 2:
        print("OPCION 2")
        i=int(input("Favor ingrese el N° de indentificacion del libro ingresado")) 
        img = qrcode.make(diccionario + i)
        type(img)  # qrcode.image.pil.PilImage2
        img.save(r'/Users/sebastiansalgado/Desktop/Seba/PROGRAMACION-nonube/qrlibros/QR-Libro-anterior.jpg') 
        answer = int (input ( "Si desea volver al menu principal marque 8  y si desea cerrar el INGRESO de libros marque 9: "))