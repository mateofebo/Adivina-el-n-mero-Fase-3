#ifndef NODO_H
#define NODO_H
#include <string>
struct Partida {
    std::string fecha, jugador1, jugador2, ganador;
    int intentos1 = 0, intentos2 = 0;
};
struct Nodo {
    Partida partida;
    Nodo* siguiente;
    explicit Nodo(const Partida& p) : partida(p), siguiente(nullptr) {}
};
void mostrarRanking(const std::string& ruta);
#endif
