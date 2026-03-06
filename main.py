from graph import Grafo
from bfs import BFS
from uniform_cost import CostoUniforme
from greedy import Greedy
from astar import AStar


def imprimir_solucion(nodo):

    camino = []

    while nodo:
        camino.append(nodo.Estado)
        nodo = nodo.Padre

    camino.reverse()

    print("Camino:", " -> ".join(camino))


if __name__ == "__main__":

    grafo = Grafo("funcion_de_costo.xlsx", "heuristica.xlsx")

    inicio = "Warm-Up"
    meta = "Stretching"

    print("=== BFS ===")
    imprimir_solucion(BFS(grafo, inicio, meta))

    print("\n=== Costo Uniforme ===")
    imprimir_solucion(CostoUniforme(grafo, inicio, meta))

    print("\n=== Greedy ===")
    imprimir_solucion(Greedy(grafo, inicio, meta))

    print("\n=== A* ===")
    imprimir_solucion(AStar(grafo, inicio, meta))