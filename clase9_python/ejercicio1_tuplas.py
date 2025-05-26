############EJERCICIOS##############
#CALCULAR EL PROMEDIOO DE LA SIGUIENTE TUPLA USANDO LAS FUNCIONES SUM(NUMEROS) Y LEN(NUMEROS)
numeros_tupla= (10,20,30,40,50,60,80,365,1)
conteo_de_todos= len(numeros_tupla)
suma_de_todos= sum(numeros_tupla)
promedio_tupla= suma_de_todos / conteo_de_todos 
print("El promedio de la tupla es: ",promedio_tupla)
print("El numero mayor de la tupla es: ",max(numeros_tupla))
print("El numero menor de la tupla es: ",min(numeros_tupla))

#NUMEROS = (10,20,30,40,50,60,80,365,1)
#ENCONTRAR EL ELEMENTO MAS GRANDE Y EL MAS PEQUEÑO EN UNA TUPLA DE NUEMEROS DE LA TUPLA ANTERIOR USANDO MAX(NUMEROS) Y MIN (NUMEROS)
#INVESTIGUE COMO CONVERTIR UNA TUPLA EN UNA LISTA, PUEDES USAR LA MISMA QUE HEMOS UTILIZADO.

#Lo primero que se debe hacer es crear la lista vacía donde se colocarán los elementos de la tupla.
#Recordemos que la lista vacía se crea simplemente igualando la variable con dos corchetes cuadrados.
lista1 = []
#Luego, vamos a crear un ciclo for que extraiga los elementos de la tupla y los agregue a la lista vacía. Será necesario usar la instrucción “len” para que el ciclo cuente sobre el total de los elementos de la tupla. Usaremos además dos instrucciones particulares:

    #La primera es extraer la entrada i-ésima de la tupla mediante corchetes: tupla[i].

    #Agregar a la lista mediante el comando append: vacia.append(tupla[i])

#Una vez terminado el ciclo for, ponemos la instrucción de imprimir la lista. Lo anterior explicado resulta:
lista2 = list(numeros_tupla)
print ("Aca convertimos de tupla a lista",lista2)
numeros_tuple2 = tuple (lista2)
print ("Aca convertimos de lista a tupla",numeros_tuple2)

lista1 = []
for i in range(len(numeros_tupla)):
	lista1.append(numeros_tupla[i])
print("Aca convertimos de tupla a lista usando un for con I  agregando cada dato  de la tupla con un append",lista1)






# Definición de tuplas con información de libros