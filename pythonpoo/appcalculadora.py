from instancias_calculadora import Calculadora

def main():
    print ("Bienvenido a la calculadora basica")
    
    try:
        Valor1=float(input("Ingrese el primer valor: "))
        Valor2=float(input("ingrese el segundo valor: "))
        
        calculadora = Calculadora (Valor1 ,Valor2)
        
        print("\nSeleccione  la operacion")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        
        opcion = input("Ingrese el numero de la operacion deseada: ")
        
        if (opcion == "1"):
            print(f"Resultadode la suma es : {calculadora.suma()}")
        elif (opcion == "2"):
            print(f"Resultado de la resta  es :{calculadora.restar()}")
        elif (opcion == "3"):
            print (f"Resultado de la multiplicacion es :{calculadora.multiplicar()}")
        elif (opcion == "4"):
            print(f"Resultado de la division es: {calculadora.dividir()}")
        else :
            print(f"Opcion no valida")
            
    except ValueError:
        print("Error: Ingrese un numero valido.")
        
if __name__ == "__main__":
    main()
    
        
        
        