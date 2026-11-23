#include "nodo.h"
#include <string>
int main(int argc, char* argv[]) {
    mostrarRanking(argc > 1 ? argv[1] : "../python_juego/historial.csv");
    return 0;
}
