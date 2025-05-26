import tkinter as teka # cambio el nombre de la libreria para abreviar la libreria
from tkinter import messagebox #traigo una variable especifica de tkinter 

class Ventana:
    
    
    def __init__(self,root):
        self.root = root
        self.root.title("Ventana con boton")
        
        
        #Crear un boton y añadirlo a la ventana
        self.boton = teka.Button(self.root,text="Haz click aqui",command=self.mostrar_mensaje)
        
        self.boton.pack(pady=20)
    
    
    def mostrar_mensaje(self):
        messagebox.showinfo("Mensaje","Hola,haz hecho tu primer programa real, con boton")
        