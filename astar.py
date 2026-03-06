from node import Nodo
from estructuras import ColaPrioridad

def AStar(grafo, inicio, meta):

    frontera = ColaPrioridad()

    nodoInicial = Nodo(inicio, costoCamino=0)
    frontera.ADD(nodoInicial)

    explorados = set()

    while not frontera.EMPTY():

        nodo = frontera.POP()

        if nodo.Estado == meta:
            return nodo

        explorados.add(nodo.Estado)

        for vecino, costo in grafo.vecinos(nodo.Estado):

            if vecino not in explorados:

                g = nodo.CostoCamino + costo
                h = grafo.h(vecino)

                hijo = Nodo(
                    estado=vecino,
                    padre=nodo,
                    accion=vecino,
                    costoCamino=g + h
                )

                frontera.ADD(hijo)

    return None