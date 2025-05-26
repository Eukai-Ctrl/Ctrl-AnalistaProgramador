# Trabajo Agenda telefonica. 'Los olvidones del codigo'
ListaNombre=[]
ListaApellido=[]
ListanumeroTelefono=[]
agenda = []
salir = False
opcion = 0

#1 Funcion para agregar contacto. 'Los olvidones del codigo'
def agregar_contacto(agenda):
    print()
    ListaNombre.append(str(input(">Ingrese el Nombre: ")))
    ListaApellido.append(str(input(">Ingrese Apellido: ")))
    ListanumeroTelefono.append(str(input(">Ingrese Numero de telefono: ")))
    agenda.append((ListaNombre[-1], ListaApellido[-1], ListanumeroTelefono[-1])) # Agrega un nuevo contacto a cada  lista y muestra el ultimo dato de cada una. 'Los olvidones del codigo'
    print('Contacto agregado correctamente')
    print()

#2 Funcion para buscar contactos. 'Los olvidones del codigo'
def buscar_nombre_contacto(agenda,nombre_buscar):
    print()       
    if nombre_buscar in ListaNombre: # Verifica si el nombre esta en la lista. 'Los olvidones del codigo'
         index = ListaNombre.index(nombre_buscar) # Busca el nombre de contacto en la lista "ListaNombre" y guarda en la variable index. 'Los olvidones del codigo'
         print("----Detalle del contacto----")
         print("Nombre del contacto:", ListaNombre[index])
         print("Apellido del contacto: ", ListaApellido[index])
         print("Telefono del contacto:", ListanumeroTelefono[index])  
         print()      
    else:
        print("El contacto", nombre_buscar, "no se encuentra en la lista de contactos.")
        print()

#3 Eliminar contacto de la lista. 'Los olvidones del codigo'
def eliminar_contacto(agenda):
    print()
    nombre_eliminar= input(">Ingrese el nombre del contacto que desea eliminar: ")
    eliminado = False  # Controla si se elimino un contacto. 'Los olvidones del codigo'
    for contacto in agenda:  # Busca por cada contacto de la agenda. 'Los olvidones del codigo'
        if contacto[0] == nombre_eliminar: # Comprueba si el nombre coincide. 'Los olvidones del codigo'
            agenda.remove(contacto)  # Elimina el contacto de la agenda. 'Los olvidones del codigo'
            #Se eliminan los datos del contacto.'Los olvidones del codigo'
            ListaNombre.remove(contacto[0])
            ListaApellido.remove(contacto[1])
            ListanumeroTelefono.remove(contacto[2])
            print("Contacto ",nombre_eliminar," fue eliminado correctamente")
            eliminado = True 
            print()
    if not eliminado:
        print("No se encontró ningún contacto con el nombre ",nombre_eliminar)
        print()

#4 Funcion para actualizar datos de contacto. 'Los olvidones del codigo'
def actualizar_contacto(agenda):
    print()
    nombre_actualizar = input(">Ingrese el nombre del contacto que desea actualizar: ")
    encontrado = False # Controla si se encontro el contacto a actualizar. 'Los olvidones del codigo' 
    for i, contacto in enumerate(agenda): #Recorre la agenda en busca del contacto. 'Los olvidones del codigo' 
        if contacto[0] == nombre_actualizar: #Verifica si coincide el nombre.'Los olvidones del codigo'
            #Se pide informacion actualizada del contacto. 'Los olvidones del codigo'
            nuevo_nombre = input("Ingrese el nuevo nombre (Presione enter si no desea actualizar): ")
            nuevo_apellido = input("Ingrese el nuevo apellido (Presione enter si no desea actualizar): ")
            nuevo_telefono = input("Ingrese el nuevo número de teléfono (Presione enter si no desea actualizar): ")
            #Se actualizan los nuevos datos del contacto. 'Los olvidones del codigo'
            if nuevo_nombre:
                ListaNombre[i] = nuevo_nombre
                agenda[i] = (nuevo_nombre, contacto[1], contacto[2])
            if nuevo_apellido:
                ListaApellido[i] = nuevo_apellido
                agenda[i] = (contacto[0], nuevo_apellido, contacto[2])
            if nuevo_telefono:
                ListanumeroTelefono[i] = nuevo_telefono
                agenda[i] = (contacto[0], contacto[1], nuevo_telefono)
            print("Contacto actualizado correctamente")
            encontrado = True
    if not encontrado:
        print("No se encontró ningún contacto con el nombre", nombre_actualizar)
    print()

#5 Funcion para ver toda la lista de contactos. 'Los olvidones del codigo'
def listado_contacto():
    print()
    for i in range(len(ListaNombre)): # Recorre la ListaNombre para imprimir la informacion de cada contacto. 'Los olvidones del codigo'
            print("----Lista de contactos----")
            print("Contacto:", i + 1) # "i" permite acceder a cada elemento de la lista uno por uno. 'Los olvidones del codigo'
            print("Nombre:", ListaNombre[i])
            print("Apellido:", ListaApellido[i])
            print("Número de teléfono:", ListanumeroTelefono[i])
            print()

# Menu de agenda. 'Los olvidones del codigo'
while (salir == False):
    print('-----Menu de opciones------')
    print('1-Agregue un nuevo contacto')
    print('2-Buscar contacto ')
    print('3-Eliminar contacto')
    print('4-Actualizar algun dato de contacto')
    print('5-Ver listado completo de contacto')
    print('6-Salir')
    opcion = int(input('Seleccione una opcion:'))
    if(opcion==6):
        salir = True
        print('Saliendo...')
    elif(opcion==1):
        agregar_contacto(agenda)
    elif(opcion==2):
        print()
        nombre_buscar=input(">Ingrese nombre de contacto que desea buscar: ")
        buscar_nombre_contacto(agenda,nombre_buscar)
    elif(opcion==3):
        eliminar_contacto(agenda)
    elif(opcion==4):
        actualizar_contacto(agenda)
    elif(opcion==5):
        listado_contacto()
    else:
        print('Opción inválida, intente nuevamente')
