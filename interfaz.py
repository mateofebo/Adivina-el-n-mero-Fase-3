"""Interfaz gráfica inicial para la Fase 3; ejecuta: python interfaz.py"""
import tkinter as tk
from tkinter import messagebox
from logica import Turno, ganador
from juego import guardar

class App:
    def __init__(self, raiz):
        self.raiz = raiz
        raiz.title("Adivina el Número")
        self.nombres = []
        self.cantidades = []
        self.indice = 0
        self.turno = None
        self.etiqueta = tk.Label(raiz, text="Jugador 1: nombre", font=("Arial", 14))
        self.etiqueta.pack(padx=20, pady=10)
        self.entrada = tk.Entry(raiz, font=("Arial", 14))
        self.entrada.pack(pady=8)
        self.mensaje = tk.Label(raiz, text="Escribe tu nombre para comenzar.", wraplength=350)
        self.mensaje.pack(pady=8)
        tk.Button(raiz, text="Aceptar / Intentar", command=self.aceptar).pack(pady=5)
        tk.Button(raiz, text="Deshacer", command=self.deshacer).pack(pady=5)
        tk.Button(raiz, text="Nueva partida", command=self.reiniciar).pack(pady=5)
        self.fase = "nombre"

    def reiniciar(self):
        self.nombres, self.cantidades, self.indice, self.turno = [], [], 0, None
        self.fase = "nombre"
        self.etiqueta.config(text="Jugador 1: nombre")
        self.mensaje.config(text="Escribe tu nombre para comenzar.")
        self.entrada.delete(0, tk.END)

    def aceptar(self):
        texto = self.entrada.get().strip()
        if self.fase == "nombre":
            self.nombres.append(texto or f"Jugador {len(self.nombres)+1}")
            self.entrada.delete(0, tk.END)
            if len(self.nombres) == 1:
                self.etiqueta.config(text="Jugador 2: nombre")
            else:
                self.iniciar_turno()
            return
        try:
            mensaje = self.turno.intentar(texto)
        except ValueError as e:
            messagebox.showerror("Entrada incorrecta", str(e))
            return
        self.mensaje.config(text=f"{mensaje} Intentos: {len(self.turno.intentos)}")
        self.entrada.delete(0, tk.END)
        if self.turno.terminado:
            self.cantidades.append(len(self.turno.intentos))
            if self.indice == 0:
                self.indice = 1
                messagebox.showinfo("Turno terminado", "Ahora juega el segundo participante.")
                self.iniciar_turno()
            else:
                resultado = ganador(self.nombres, self.cantidades)
                guardar(self.nombres, self.cantidades, resultado)
                messagebox.showinfo("Resultado", f"Ganador: {resultado}\nIntentos: {self.cantidades}\nResultado guardado en CSV.")
                self.fase = "final"
                self.mensaje.config(text="Partida terminada. Pulsa Nueva partida.")

    def iniciar_turno(self):
        self.turno = Turno()
        self.fase = "juego"
        self.etiqueta.config(text=f"Turno de {self.nombres[self.indice]}")
        self.mensaje.config(text="Adivina un número del 1 al 20.")

    def deshacer(self):
        if self.fase != "juego":
            return
        try:
            n = self.turno.deshacer()
            self.mensaje.config(text=f"Intento {n} deshecho. Quedan {len(self.turno.intentos)} intentos.")
        except ValueError as e:
            messagebox.showinfo("Deshacer", str(e))

if __name__ == "__main__":
    raiz = tk.Tk()
    App(raiz)
    raiz.mainloop()
