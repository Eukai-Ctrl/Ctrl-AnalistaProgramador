#calcular la cantidad de dias vividos incluyendo los dias bisiestos
año_nacimiento = int(input("Favor ingrese su año de nacimiento: "))
año_tope = int(2024)
calcul = int() #CALCULAR SI AÑO ES BISIESTO O NO
calcul2 = int() # CALCULAR TOTAL DE DIAS VIVIDOS
calcul2 = 0
calcul3 = 0
calcul4 = int()
while año_nacimiento < año_tope:
    año_nacimiento += 1
    calcul = año_nacimiento % 4
    if calcul > 0:
       calcul2 += 365
    elif calcul == 0:
        calcul3 += 366
    
    calcul4 = calcul2+calcul3
print("Segun el año ingresado usted ha vivido ",calcul4," dias ")