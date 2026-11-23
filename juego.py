import csv
from datetime import datetime
from pathlib import Path
from logica import Turno, ganador

HISTORIAL = Path(__file__).with_name("historial.csv")
CAMPOS = ["fecha", "jugador1", "intentos1", "jugador2", "intentos2", "ganador"]

def guardar(nombres, cantidades, resultado):
    nuevo = not HISTORIAL.exists() or HISTORIAL.stat().st_size == 0
    with HISTORIAL.open("a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        if nuevo:
            writer.writerow(CAMPOS)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), nombres[0], cantidades[0], nombres[1], cantidades[1], resultado])

def partida():
    nombres = [input(f"Nombre del jugador {i}: ").strip() for i in (1, 2)]
    nombres = [n or f"Jugador {i}" for i, n in enumerate(nombres, 1)]
    cantidades = []
    for nombre in nombres:
        turno = Turno()
        print(f"\nTurno de {nombre}. Adivina del 1 al 20; D deshace.")
        while not turno.terminado:
            entrada = input("Número o D: ").strip()
            try:
                if entrada.upper() == "D":
                    print("Deshecho:", turno.deshacer())
                else:
                    print(turno.intentar(entrada))
                    print("Intentos:", len(turno.intentos))
            except ValueError as e:
                print("Error:", e)
        cantidades.append(len(turno.intentos))
    resultado = ganador(nombres, cantidades)
    print("\nResultados:", dict(zip(nombres, cantidades)), "| Ganador:", resultado)
    guardar(nombres, cantidades, resultado)
    print("Guardado en", HISTORIAL)

def main():
    while True:
        print("\n=== ADIVINA EL NÚMERO ===")
        print("1. Jugar | 2. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            partida()
        elif opcion == "2":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
