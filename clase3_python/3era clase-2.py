num = int()
num = int(input("ingrese un numero de 1 al 10"))
while num < 1 or num > 10:
    print("ERROR, NUMERO INGRESADO ES INVALIDO")
    num = int(input("Reingrese un numero del 1 al 10: "))



#valida contraseña de netflix, tiene que tener un largo 4-6 caracteres maximo 3 intento
#invalido, despues de esto se bloquea la cuenta. 