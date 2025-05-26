from instancia_persona import Persona

#creamos nuestros objetos personas

objPersonaUno = Persona (16, 75.3, 165.3, "Cristobal")
objPersonaDos = Persona (18,60.3,155.9,"Valeria")
objPersonaTres = Persona(35,80.5,178.3,"Diego")

print( 'Datos persona Uno.')
objPersonaUno.mostrar()
print(f"¿Es mayor de edad ?{'Si'if objPersonaUno.mayor() else 'No'}\n") #el \n es como un enter en el codigo como un salto 

print( 'Datos persona Dos.')
objPersonaDos.mostrar()
print(f"¿Es mayor de edad ?{'Si'if objPersonaDos.mayor() else 'No'}\n")

print( 'Datos persona Tres.')
objPersonaTres.mostrar()
print(f"¿Es mayor de edad ?{'Si'if objPersonaTres.mayor() else 'No'}\n")


