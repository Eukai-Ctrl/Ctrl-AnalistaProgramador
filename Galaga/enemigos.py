import tkinter as tk
import random

class Enemigos:

    def __init__(self, canvas, num_enemigos=5):
        self.canvas = canvas
        self.enemigos = []
        self.num_enemigos = num_enemigos

        self.canvas.after(100, self.generar_enemigos)
    
    def generar_enemigos(self):
        for _ in range(self.num_enemigos):
            x = random.randint(50, self.canvas.winfo_width() - 50)
            y = random.randint(50,150)
            enemigo = self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="blue")
            self.enemigos.append(enemigo)

    def mover(self):
        for enemigo in self.enemigos:
            x1,y1,x2,y2 = self.canvas.coords(enemigo)
            self.canvas.move(enemigo, 0, 2)
    
    def colision(self, balas):
        for bala in balas:
            x1,y1,x2,y2 = self.canvas.coords(bala)
            for enemigo in self.enemigos:
                ex1,ey1,ex2,ey2 = self.canvas.coords(enemigo)
                if x1 < ex2 and x2 > ex1 and y1 < ey2 and y2 > ey1:
                    self.canvas.delete(enemigo)
                    self.canvas.delete(bala)
                    self.enemigos.remove(enemigo)
                    balas.remove(bala)
                    break