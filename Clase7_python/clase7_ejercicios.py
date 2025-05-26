#metodo append
lista = ["jorge","Sepulveda",25,1,2002]
i = int()
#for i in range (5):
    #print(lista[i])
#la funcion append permite agregar a la ultima posicion de la lista un nuevo elemento
lista.append("Renca")
#for i in range (6):
    #print(lista[i])
#La funcion insert permite agregar a una posicion de la lista un nuevo elemento
lista.insert(0,"Manuel")
lista.insert(3,"Vasquez")

#for i in range (8):
    #print(lista[i])

#La funcion count, permite "contar" la cantidad de  veces que se repite el dato indicado en el count
x = lista.count(25)
print("Valor Count: ",x)

#La funcion remove, permite " eliminar" el dato indicado en el remove
lista.remove(2002)
#La funcion pop, permite eliminar el dato pero indicando la posicion  a diferencia del remove que es indicando el dato directamente
lista.pop(0)
#La funcion index, nos muestra en que posicion de la lista se encuentra un dato especifico 
y = lista.index("Renca")

for i in range (6):
    print(lista[i])

print("Renca esta en la posicion: ",y)

