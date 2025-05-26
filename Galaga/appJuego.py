import tkinter as tk
from nave import Nave
from enemigos import Enemigos

class JuegoGalaga:

    def __init__(self, root):
        self.root = root
        self.root.title("Juego Galaga POO")
        self.canvas = tk.Canvas(self.root, width=500, height=600, bg="black")
        self.canvas.pack()

        self.nave = Nave(self.canvas, 250,550)
        self.enemigos = Enemigos(self.canvas, num_enemigos=5)
        self.balas = []

        self.root.bind("<Left>", self.nave.mover_izquierda)
        self.root.bind("<Right>", self.nave.mover_derecha)
        self.root.bind("<space>", lambda event: self.nave.disparar(self.balas))

        self.root.after(150, self.actualizar)
    
    def actualizar(self):
        #Moves balas hacia arriba
        for bala in self.balas:
            self.canvas.move(bala, 0, -10)
            x1, x2, y1, y2 = self.canvas.coords(bala)
            if y2 < 0:
                self.canvas.delete(bala)
                self.balas.remove(bala)
        
        #mover enemigos y detectar colisiones
        self.enemigos.mover()
        self.enemigos.colision(self.balas)

        #Verificar si enemigos fueron eliminados
        if not self.enemigos.enemigos:
            self.canvas.create_text(250, 300, text="¡Has Ganado!, you Win!!!", fill="white", font=("Arial", 24))
            return

        #continuar el bucle del juego
        self.root.after(50, self.actualizar)

if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoGalaga(root)
    root.mainloop() 