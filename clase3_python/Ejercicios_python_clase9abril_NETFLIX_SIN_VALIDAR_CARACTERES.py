#valida contraseña de netflix, tiene que tener un largo 4-6 caracteres maximo 3 intento
#invalido, despues de esto se bloquea la cuenta. 
#clave = str(input("Favor ingresar su clave de netflix, recordar que esta no puede ser de mas de 6 caracteres ni menos de 4"))
clave = ("Renca")
#validarr = False
contador_intento = int(0)
intentos_restantes = (2)
while contador_intento < 3:
 Banner_ingreso =str(input("Favor ingresar su clave de acceso: "))
 #validador de cantidad de caracteres



 if  Banner_ingreso== (clave):#Banner_ingreso == ("R" and "e" and "n" and "c" or "a"):
    print("Acceso habilitado,clave correcta")
    contador_intento += 4
 else:
   print("Clave incorrecta,intentelo nuevamante,le quedan ",intentos_restantes," intentos ")
   contador_intento += 1
   intentos_restantes -= 1