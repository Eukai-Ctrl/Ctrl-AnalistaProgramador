original_1 = str("c")
original_2 = str("a")
original_3 = str("s")
original_4 = str("a")
i1 = str()
i2 = str()
i3 = str()
i4 = str()


veces = int(2) #oportunidad de fallos

while veces >= 0:
    i1 = str(input("ingrese caracter clave 1: "))
    i2 = str(input("ingrese caracter clave 2: "))
    i1 = str(input("ingrese caracter clave 3: "))
    i4 = str(input("ingrese caracter clave 4: "))
    if original_1 == i1 and original_1 == i2 and original_3 == i3 and original_4 == i4:
        print("tutummm has ingresado a tu cuenta...")
        veces = 0
print("Clave bloqueda : Contactarse con el dueño de la cuenta")


