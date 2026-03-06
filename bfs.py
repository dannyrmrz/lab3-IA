from node import Nodo
from estructuras import ColaFIFO

def BFS(grafo, inicio, meta):

    frontera = ColaFIFO()
    frontera.ADD(Nodo(inicio))
    explorados = set()

    while not frontera.EMPTY():

        nodo = frontera.POP()

        if nodo.Estado == meta:
            return nodo

        explorados.add(nodo.Estado)

        for vecino, costo in grafo.vecinos(nodo.Estado):

            if vecino not in explorados:
                hijo = Nodo(
                    estado=vecino,
                    padre=nodo,
                    accion=vecino,
                    costoCamino=nodo.CostoCamino + costo
                )
                frontera.ADD(hijo)

    return None