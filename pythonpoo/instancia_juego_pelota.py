import tkinter as teka

class Juego_Pelota:
    
    def __init__(self,VentanaPrincipal):
        
        self.VentanaPrincipal = VentanaPrincipal
        self.VentanaPrincipal.title("Juego de la pelota.")
        
        self.canvas = teka.Canvas(self.VentanaPrincipal,width=500,height=400,bg="white")
        self.canvas.pack()
        
        self.pelota = self.canvas.create_oval(240,190,260,210,fill="blue")
        
        self.VentanaPrincipal.bind("<Up>",self.mover_arriba)
        self.VentanaPrincipal.bind("<Down>",self.mover_abajo)
        self.VentanaPrincipal.bind("<Left>",self.mover_izquierda)
        self.VentanaPrincipal.bind("<Right>",self.mover_derecha)
        self.VentanaPrincipal.bind("<space>",self.saltar)
    
    def mover_arriba(self,event):
        x1,y1,x2,y2,= self.canvas.coords(self.pelota)
        if y1 > 0:
            self.canvas.move(self.pelota,0,-10)
    
    def mover_abajo(self,event):
        x1,y1,x2,y2,= self.canvas.coords(self.pelota)
        if y2 < 400:
            self.canvas.move(self.pelota,0,10)
    
    def mover_izquierda (self,event):
        x1,y1,x2,y2,= self.canvas.coords(self.pelota)
        if x1 > 0:
            self.canvas.move(self.pelota,-10,0)
    
    def mover_derecha (self,event):
        x1,y1,x2,y2,= self.canvas.coords(self.pelota)
        if x2 < 500:
            self.canvas.move(self.pelota,10,0)
    def saltar(self,event):
        for _ in range(10):
            x1,y1,x2,y2,= self.canvas.coords(self.pelota)
        if y1 > 0:
            self.canvas.move(self.pelota,0,-5)
            self.VentanaPrincipal.update()
            self.canvas.after(30)
        for _ in range(10):
            x1,y1,x2,y2,= self.canvas.coords(self.pelota)
        if y2 < 400:
            self.canvas.move(self.pelota,0,5)
            self.VentanaPrincipal.update()
            self.canvas.after(30)
