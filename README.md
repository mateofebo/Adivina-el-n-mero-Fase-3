# Adivina el Número — Fase 3

Proyecto integrador de Lógica de Programación. Integrantes: Mateo Fernández y Diego García.

## Descripción
Juego para dos personas: cada participante adivina un número secreto entre 1 y 20. Gana quien acierte con menos intentos. El historial de resultados se comparte con C++ mediante CSV.

## Estructura
- `python_juego/logica.py`: validaciones, pila de intentos y vector de estados.
- `python_juego/juego.py`: versión de consola y registro CSV.
- `python_juego/interfaz.py`: interfaz gráfica inicial con Tkinter.
- `python_juego/historial.csv`: encabezado de resultados (se añaden filas al jugar).
- `cpp_datos/nodo.h`: nodo de lista enlazada simple.
- `cpp_datos/ranking.cpp`: lectura del CSV, lista enlazada y burbuja.
- `cpp_datos/main.cpp`: punto de entrada de C++.
- `diagramas/`: documentación de fases anteriores.
- `docs/BITACORA.md`: plantilla de bitácora que debe verificarse con hechos reales.
- Video explicativo de Fase 3: enlace de Google Drive en la sección siguiente.

## Video explicativo de la Fase 3
[Ver video explicativo en Google Drive](https://drive.google.com/file/d/1aZEozr-VNM_V463jvc8mlbIOYrxPNRoc/view?usp=
## Ejecutar
Se requiere Python 3 con Tkinter y compilador C++17.

```bash
python python_juego/juego.py
python python_juego/interfaz.py
# Desde la carpeta raíz del proyecto:
g++ -std=c++17 cpp_datos/main.cpp cpp_datos/ranking.cpp -o ranking
./ranking python_juego/historial.csv
```

En Windows, ejecutar `ranking.exe python_juego/historial.csv`.

## Contrato CSV
Separador `;`. Columnas: `fecha;jugador1;intentos1;jugador2;intentos2;ganador`.
Cada partida tiene un número secreto diferente por jugador. El deshacer retira un intento del contador, aunque no elimina la pista que el jugador ya vio.

## Autoría, créditos y uso de IA
Trabajo del equipo Mateo Fernández y Diego García. Se utilizó ChatGPT (OpenAI) como apoyo para elaborar borradores de código, documentación y organización del proyecto. Los integrantes deben revisar, comprender y probar el contenido antes de entregarlo. Python, Tkinter y C++ son tecnologías usadas; consultar sus respectivas documentaciones oficiales. No se incorporaron imágenes de terceros en el código.

## Licencia
Se incluye una propuesta de licencia MIT en `LICENSE`; ambos integrantes deben aprobarla antes de publicar el repositorio.

## Estado
Prototipo inicial de Fase 3. Revisar la integración, la interfaz y los casos de prueba en el equipo antes de la entrega.
