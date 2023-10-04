import tkinter as tk
import random

class BatallaNaval:
    def __init__(self, ventana, filas=8, columnas=8, num_barcos=4, longitud_barcos=3):
        self.ventana = ventana
        self.ventana.title("Batalla Naval")
        self.filas = filas
        self.columnas = columnas
        self.num_barcos = num_barcos
        self.longitud_barcos = longitud_barcos
        self.tablero = [['O' for _ in range(self.columnas)] for _ in range(self.filas)]

        # Colocar barcos en el tablero
        self.colocar_barcos()

        # Crear etiquetas para el tablero
        self.etiquetas = [[None for _ in range(self.columnas)] for _ in range(self.filas)]
        for i in range(self.filas):
            for j in range(self.columnas):
                self.etiquetas[i][j] = tk.Label(ventana, text=' ', width=2, height=1, borderwidth=1, relief="solid")
                self.etiquetas[i][j].grid(row=i, column=j)

        # Etiqueta para el estado del juego
        self.etiqueta_estado = tk.Label(ventana, text="¡Buena suerte!", padx=10)
        self.etiqueta_estado.grid(row=self.filas, columnspan=self.columnas)

        # Entradas para las coordenadas del ataque
        self.fila_label = tk.Label(ventana, text="Fila:")
        self.fila_label.grid(row=self.filas + 1, column=0)
        self.fila_entry = tk.Entry(ventana)
        self.fila_entry.grid(row=self.filas + 1, column=1)

        self.columna_label = tk.Label(ventana, text="Columna:")
        self.columna_label.grid(row=self.filas + 2, column=0)
        self.columna_entry = tk.Entry(ventana)
        self.columna_entry.grid(row=self.filas + 2, column=1)

        # Botón para realizar ataques
        self.boton_atacar = tk.Button(ventana, text="Atacar", command=self.atacar)
        self.boton_atacar.grid(row=self.filas + 3, columnspan=self.columnas)

        # Mostrar el tablero inicial
        self.mostrar_tablero()

    def colocar_barcos(self):
        for _ in range(self.num_barcos):
            self.colocar_barco()

    def colocar_barco(self):
        fila_inicio = random.randint(0, self.filas - 1)
        columna_inicio = random.randint(0, self.columnas - 1)
        direccion = random.choice(['horizontal', 'vertical'])

        if direccion == 'horizontal':
            while columna_inicio + self.longitud_barcos > self.columnas:
                columna_inicio = random.randint(0, self.columnas - 1)
        else:
            while fila_inicio + self.longitud_barcos > self.filas:
                fila_inicio = random.randint(0, self.filas - 1)

        if direccion == 'horizontal':
            for i in range(self.longitud_barcos):
                self.tablero[fila_inicio][columna_inicio + i] = 'B'
        else:
            for i in range(self.longitud_barcos):
                self.tablero[fila_inicio + i][columna_inicio] = 'B'

    def mostrar_tablero(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                self.etiquetas[i][j].config(text=self.tablero[i][j])

    def atacar(self):
        fila = int(self.fila_entry.get())
        columna = int(self.columna_entry.get())

        if self.tablero[fila][columna] == 'B':
            self.tablero[fila][columna] = 'X'
            self.mostrar_tablero()
            self.etiqueta_estado.config(text="¡Hundiste un barco!")
        else:
            self.tablero[fila][columna] = ' '
            self.mostrar_tablero()
            self.etiqueta_estado.config(text="¡Agua!")

if __name__ == "__main__":
    ventana = tk.Tk()
    juego = BatallaNaval(ventana)
    ventana.mainloop()
