#probando el range con un solo argumento}
#del 1 al 10
num = int()
num1 = int()
num2 = int()
num3 = int()
num4 = int()


for num in range (10):
    print("con un argumento - Voy en la vuelta N°: ",num)
    
for num1 in  range(1,15):
    print("con 2 argumento - Voy en la vuelta N°: ",num1)

for num2 in  range(5,50,5):
    print("con 3 argumento - Voy en la vuelta N°: ",num2)

#EJERCICIOS 
#PROGRAMA DONDE DEBO INGRESAR VALORES POR TECLADO 
# UNA INCREMENTADORA Y OTRA DECREMENTADORA  EN EL MISMO PROGRAMA
a = int(input("Favor ingresar START"))
b = int(input("Favor ingresar STOP"))
c = int(input("Favor ingresar STEP"))
for num3  in range (a,b,c,):
     print("con 3 argumentos - incrementando de : ",c,"Valor :",num1)


a = int(input("Favor ingresar START"))
b = int(input("Favor ingresar STOP"))
c = int(input("Favor ingresar STEP"))

for num4 in range (a,b,-(c)):
     print("con 3 argumentos - decrementando de : ",c,"Valor :",num2)


