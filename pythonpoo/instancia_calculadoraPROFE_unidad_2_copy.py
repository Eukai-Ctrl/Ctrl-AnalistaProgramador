import tkinter as tk
from tkinter import messagebox
from math import sqrt

class VentanaSuma:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculando 2 numeros")

        tk.Label(self.root, text="Número: 1:").pack(pady=5)
        self.numero1 = tk.Entry(self.root)
        self.numero1.pack(pady=5)

        tk.Label(self.root, text="Número: 2:").pack(pady=5)
        self.numero2 = tk.Entry(self.root)
        self.numero2.pack(pady=5)

        tk.Label(self.root, text="Operacion").pack(pady=5)
        self.operacion = tk.Entry(self.root)
        self.operacion.pack(pady=5)


        self.boton_calcular = tk.Button(self.root, text="Calcular", command=self.calcular)
        self.boton_calcular.pack(pady=10)

    def calcular(self):
        num1 = float(self.numero1. get())
        num2 = float(self.numero2. get())
        operacion= str(self.operacion. get())
        #operacion = self.operacion.get().strip()
        if (operacion == "+"):
            messagebox.showinfo("Resultado", f"el resultado de la suma es : {num1+num2}")
            print(f"Resultadode la suma es : {num1+num2}")
        elif (operacion == "-"):
            messagebox.showinfo("Resultado", f"el resultado de la resta es : {num1-num2}")
            print(f"Resultado de la resta  es :{num1-num2}")
        elif (operacion == "*"):
            messagebox.showinfo("Resultado", f"el resultado de la resta es : {num1*num2}")
            print (f"Resultado de la multiplicacion es :{num1*num2}")
        elif (operacion == "/"):
            messagebox.showinfo("Resultado", f"el resultado de la resta es : {num1/num2}")
            print(f"Resultado de la division es: {num1/num2}")
        elif (operacion == "r"):
            messagebox.showinfo("Resultado", f"el resultado de la resta es : {sqrt(num1),sqrt(num2)}")
            print(f"Resultado de la raiz es: {sqrt(num1),sqrt(num2)}")
        elif (operacion == "p"):
            messagebox.showinfo("Resultado", f"el resultado de la resta es : {num1**num2}")
            print(f"Resultado de la potencia es: {num1**num2}")
        else :
            print(f"Opcion no valida")