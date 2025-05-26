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

        #tk.Label(self.root, text="Operacion").pack(pady=5)
        #self.operacion = tk.Entry(self.root)
        #self.operacion.pack(pady=5)


        self.boton_calcular = tk.Button(self.root, text="Calcular", command=self.calcular)
        self.boton_calcular.pack(pady=10)

    def calcular(self):
        try:
            num1 = float(self.numero1. get())
            num2 = float(self.numero2. get())

            rs = num1+num2
            rs1= num1-num2
            rs2= num1*num2
            rs3= num1/num2
            rs4= sqrt(num1) 
            rs4_1= sqrt(num2)
            rs5= num1**num2

            messagebox.showinfo("Resultado", f"el resultado de la suma es : {rs}")
            messagebox.showinfo("Resultado", f"el resultado de la resta es : {rs1}")
            messagebox.showinfo("Resultado", f"el resultado de la multiplicacion es : {rs2}")
            messagebox.showinfo("Resultado", f"el resultado de la division es : {rs3}")
            messagebox.showinfo("Resultado", f"el resultado de la raiz primer numero es : {rs4}")
            messagebox.showinfo("Resultado", f"el resultado de la raiz segundo es : {rs4_1}")
            messagebox.showinfo("Resultado", f"el resultado de la elevacion es : {rs5}")
        except ValueError:
            messagebox.showerror("error", "ingresa un número váliado")