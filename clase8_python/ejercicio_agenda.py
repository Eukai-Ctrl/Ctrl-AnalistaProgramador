# Listas para almacenar los contactos
listaNombre=["Andres"]
listaApellido=["Navarro"]
listaTelefono=[912345678]
x=int()
bucle=str("SI")

while bucle=="SI" or bucle=="si":
    print("Bienvenido a la Agenda Online")
    x=int(input("¿Cuántos registros le gustaría hacer?: "))

    # Para agregar registros
    for x in range(x):
        listaNombre.append(str(input("Ingrese Nombre: ")))
        listaApellido.append(str(input("Ingrese su Apellido: ")))
        listaTelefono.append(str(input("Ingrese su Telefono: ")))  