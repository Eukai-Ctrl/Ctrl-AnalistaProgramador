#el primer valor de una tupla es el 0.
#las tuplas son similares a las listas pero no se pueden agregar ni modificar los datos
#funciones que podemos usar en una tupla: len(),index(),count(),+(concatenacion),*(repeticicion)
#Definición de tuplas con información de libros libro1 = ("El Señor de los Anillos", "J.R.R. Tolkien", 1954, 1000)

############EJERCICIOS##############
#CALCULAR EL PROMEDIOO DE LA SIGUIENTE TUPLA USANDO LAS FUNCIONES SUM(NUMEROS) Y LEN(NUMEROS)
#NUMEROS = (10,20,30,40,50,60,80,365,1)
#ENCONTRAR EL ELEMENTO MAS GRANDE Y EL MAS PEQUEÑO EN UNA TUPLA DE NUEMEROS DE LA TUPLA ANTERIOR USANDO MAX(NUMEROS) Y MIN (NUMEROS)
#INVESTIGUE COMO CONVERTIR UNA TUPLA EN UNA LISTA, PUEDES USAR LA MISMA QUE HEMOS UTILIZADO.
# Definición de tuplas con información de libros
libro1 = ("El Señor de los Anillos", "J.R.R. Tolkien", 1954, 1000)
libro2 = ("Cien años de soledad", "Gabriel García Márquez", 1967, 800)
libro3 = ("Harry Potter y la Piedra Filosofal", "J.K. Rowling", 1997, 600)
# Mostrar la información de los libros
print("Información de los libros:")
for libro in [libro1, libro2, libro3]:
 titulo, autor, año, paginas = libro
 print(f"Título: {titulo}, Autor: {autor}, Año: {año}, Páginas: {paginas}")
 # Concatenar tuplas para crear una lista de todos los libros
 todos_libros = libro1 + libro2 + libro3
 # Contar cuántos libros hay en total
 total_libros = len(todos_libros)
 # Encontrar el libro más antiguo
 libro_mas_antiguo = min([libro[2] for libro in [libro1, libro2, libro3]])
 print(f"\nTotal de libros en la biblioteca: {total_libros}")
 print(f"El año del libro más antiguo en la biblioteca es: {libro_mas_antiguo}")
 #LOS OBJETOS SON UNA REPRESENTACION DE CUALQUIERA COSA. ES UNA REPRESENTACION DE ALGO
 #TIENE ELEMENTOS Y COMPORTAMIENTOS // (ATRIBUTOS) EJ: COLOR,VELOCIDAD,RUEDAS [DESCRIPTORES] Y (METODOS)  EJ: ARRANCA(), FRENA() , DOBLAR() [ACCIONES]