radio = float()
pi = float(3.1416)
area = float()
bisiesto = int()
cont = int()
dias = int()




print("******MENU*******")
print("Opcion 1 :")
print("Opcion 2 :")
print("Opcion 3 :")
print("Opcion 4 :")
print("Opcion 5 :")

opc = int (input("Ingrese opcion seleccionada"))
if opc == 1:
    radio = float(input("Ingrese el radio del circulo"))
    area = pi * (radio**2)
    print("el area del circulo es : ",area)
elif opc == 2:
    radio = float (input("Ingrese el radio del ciruclo"))
    diametro = radio * 2
    print("El diametro del circulo es: ",diametro)
elif opc ==3:
    altura = float(input("ingrese el valor de la altura"))
    base = float(input("ingrese el valor de la base"))
    area_tri = (base * altura)/2
    print("el area del triangulo es : ",area_tri)
elif opc == 4:
    nac_mama = int(input("Favor ingresar el año nacimiento de la madre"))
    nac_hijo = int(input("favor ingresar el año de nacimiento del hijo"))
    nac_nac = nac_hijo - nac_mama
    print("La edad de la madre al tener el hijo es :",nac_nac,"años.")
elif opc == 5 :
    nac = int(input("ingrese su año de nacimiento"))
    while nac <= 2024:
        if nac % 4 == 0:
            print(nac)
            bisiesto+=1
        cont += 1
        nac+=1
    dias = cont * 365
    print ( " los dias vividos son:",dias,"dias  y los dias de años bisiestos son:",bisiesto,"y en total:",dias+bisiesto)
    print("años vividos: ",cont)

