import random

def secreto_nuevo():
    return random.randint(1, 20)

def validar(texto):
    try:
        n = int(texto.strip())
    except (ValueError, AttributeError):
        raise ValueError("Ingresa un número entero, no letras.")
    if not 1 <= n <= 20:
        raise ValueError("El número debe estar entre 1 y 20.")
    return n

class Turno:
    def __init__(self):
        self.secreto = secreto_nuevo()
        self.intentos = []  # pila LIFO
        self.estados = [0] * 20  # 0 sin usar, 1 bajo, 2 alto, 3 acierto
        self.terminado = False

    def intentar(self, texto):
        if self.terminado:
            raise ValueError("El turno ya terminó.")
        n = validar(texto)
        self.intentos.append(n)
        estado = 1 if n < self.secreto else 2 if n > self.secreto else 3
        self.estados[n - 1] = estado
        self.terminado = estado == 3
        return "¡Correcto!" if estado == 3 else "El número secreto es mayor." if estado == 1 else "El número secreto es menor."

    def deshacer(self):
        if self.terminado or not self.intentos:
            raise ValueError("No se puede deshacer este intento.")
        anterior = self.intentos.pop()
        self.estados[anterior - 1] = next((1 if x < self.secreto else 2 if x > self.secreto else 3 for x in reversed(self.intentos) if x == anterior), 0)
        return anterior

def ganador(nombres, cantidades):
    return nombres[0] if cantidades[0] < cantidades[1] else nombres[1] if cantidades[1] < cantidades[0] else "Empate"
