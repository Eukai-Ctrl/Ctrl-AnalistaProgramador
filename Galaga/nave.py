import tkinter as tk

class Nave:

    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.nave = self.canvas.create_rectangle(x - 20, y - 10, x + 10, y + 10, fill="green")
        self.velocidad = 20

    def mover_izquierda(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.nave)
        if x1 > 0:
            self.canvas.move(self.nave, -self.velocidad, 0)

    def mover_derecha(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.nave)
        if x2 < self.canvas.winfo_width():
            self.canvas.move(self.nave, self.velocidad, 0)

    def disparar(self, balas):
        x1, y1, x2, y2 = self.canvas.coords(self.nave)
        bala = self.canvas.create_oval((x1 + x2) / 2 - 2, y1 - 10, (x1 + x2) / 2 + 2, y1, fill="red" )
        balas.append(bala)