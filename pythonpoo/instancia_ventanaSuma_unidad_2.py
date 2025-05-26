import tkinter as teka # cambio el nombre de la libreria para abreviar la libreria
from tkinter import messagebox

class ventanaOperaciones:
    def __init__(self,ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.ventanaPrincipal.title("Calculadora")
        
        
        teka.Label(self.ventanaPrincipal,text="Numero: 1: ").pack(pady=5)
        self.numero1=teka.Entry(self.ventanaPrincipal)
        self.numero1.pack(pady=5)
        
        teka.Label(self.ventanaPrincipal,text="Numero: 2: ").pack(pady=5)
        self.numero2=teka.Entry(self.ventanaPrincipal)
        self.numero2.pack(pady=5)
        
        
        self.boton_sumar = teka.Button(self.ventanaPrincipal,text="Sumar",command=self.sumar)
        self.boton_sumar.pack(pady=10)
        
        self.boton_restar = teka.Button(self.ventanaPrincipal,text="Restar",command=self.restar)
        self.boton_restar.pack(pady=10)
    
    
    def sumar(self):
        try:
            num1suma=float(self.numero1.get())
            #num1= self.numero1
            #num2= self.numero2
            num2suma=float(self.numero2.get())
            rs_suma= num1suma + num2suma
            messagebox.showinfo("Resultado",f"La suma es: {rs_suma}")
            
        except ValueError:
            messagebox.showerror("Error","Ingresa un numerosvalido")
    def restar(self):
        try:
            num1resta=float(self.numero1.get())
            #num1= self.numero1
            #num2= self.numero2
            num2resta=float(self.numero2.get())
            rs_resta = num1resta - num2resta
            messagebox.showinfo("Resultado",f"La resta es: {rs_resta}")
            
        except ValueError:
            messagebox.showerror("Error","Ingresa un numerosvalido")
            