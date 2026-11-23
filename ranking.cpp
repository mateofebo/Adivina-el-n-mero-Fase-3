#include "nodo.h"
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
#include <utility>

bool leer(const std::string& linea, Partida& p) {
    std::stringstream ss(linea);
    std::string i1, i2;
    if (!std::getline(ss, p.fecha, ';') || !std::getline(ss, p.jugador1, ';') ||
        !std::getline(ss, i1, ';') || !std::getline(ss, p.jugador2, ';') ||
        !std::getline(ss, i2, ';') || !std::getline(ss, p.ganador)) return false;
    try { p.intentos1 = std::stoi(i1); p.intentos2 = std::stoi(i2); }
    catch (...) { return false; }
    return true;
}

void sumar(std::vector<std::pair<std::string,int>>& ranking, const std::string& nombre) {
    for (auto& x : ranking) if (x.first == nombre) { ++x.second; return; }
    ranking.push_back({nombre, 1});
}

void mostrarRanking(const std::string& ruta) {
    std::ifstream archivo(ruta);
    if (!archivo) { std::cerr << "No se puede abrir: " << ruta << "\n"; return; }
    Nodo* cabeza = nullptr;
    Nodo* ultimo = nullptr;
    std::string linea;
    std::getline(archivo, linea); // encabezado CSV
    int partidas = 0;
    while (std::getline(archivo, linea)) {
        Partida p;
        if (!leer(linea, p)) continue;
        Nodo* nuevo = new Nodo(p);
        if (!cabeza) cabeza = nuevo;
        else ultimo->siguiente = nuevo;
        ultimo = nuevo;
        ++partidas;
    }
    std::vector<std::pair<std::string,int>> ranking;
    for (Nodo* actual = cabeza; actual; actual = actual->siguiente) {
        const Partida& p = actual->partida;
        if (p.ganador == p.jugador1 && p.ganador != "Empate") sumar(ranking, p.jugador1);
        else if (p.ganador == p.jugador2 && p.ganador != "Empate") sumar(ranking, p.jugador2);
    }
    // Burbuja: mayor cantidad de victorias primero.
    for (size_t i = 0; i < ranking.size(); ++i)
        for (size_t j = 0; j + 1 < ranking.size() - i; ++j)
            if (ranking[j].second < ranking[j+1].second)
                std::swap(ranking[j], ranking[j+1]);
    std::cout << "=== RANKING ===\nPartidas: " << partidas << "\n";
    for (size_t i = 0; i < ranking.size(); ++i)
        std::cout << i+1 << ". " << ranking[i].first << " - " << ranking[i].second << " victorias\n";
    if (ranking.empty()) std::cout << "Todavía no hay victorias registradas.\n";
    while (cabeza) { Nodo* siguiente = cabeza->siguiente; delete cabeza; cabeza = siguiente; }
}
