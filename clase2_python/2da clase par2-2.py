nac = int()
edad = int()

nac = int(input('Ingrese en que año nacio ud. : '))

edad  = 2024 - nac 
if edad <= 3 : # este es un SI, debe quedar respetando las tabulaciones para que entre
    print('Ud es un lactante de edad y tiene ',edad,'años')
elif  edad <= 10:    # es la forma de hacer SEGUN  es una variacion de if-else 
    print('Ud es niño de edad y tiene ',edad,'años')
elif  edad <= 14:    # es la forma de hacer SEGUN  es una variacion de if-else 
    print('Ud es puber de edad y tiene ',edad,'años')
elif  edad <= 18:    # es la forma de hacer SEGUN  es una variacion de if-else 
    print('Ud es adolescente de edad y tiene ',edad,'años')
elif  edad <= 35:    # es la forma de hacer SEGUN  es una variacion de if-else 
    print('Ud es joven de edad y tiene ',edad,'años')
elif  edad <= 45:    # es la forma de hacer SEGUN  es una variacion de if-else 
    print('Ud es joven-adulto de edad y tiene ',edad,'años y necesita ibuprofeno')
elif  edad <= 60:    # es la forma de hacer SEGUN  es una variacion de if-else 
    print('Ud es adulto de edad y tiene ',edad,'años y necesita ibuprofeno')  
elif  edad <= 120:    # es la forma de hacer SEGUN  es una variacion de if-else 
    print('Ud es anciano de edad y tiene ',edad,'años y necesita tramadol')

    # usando el elif no es necesario cerrar el if con un else ya que es una lista de opciones " SEGUN" por lo que se usa elif de manera constante             
# SENTENCIAS DE CONTROL 