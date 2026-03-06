from node import Nodo
from estructuras import ColaPrioridad

def Greedy(grafo, inicio, meta):

    frontera = ColaPrioridad()
    nodoInicial = Nodo(inicio)
    nodoInicial.CostoCamino = grafo.h(inicio)
    frontera.ADD(nodoInicial)

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
                    costoCamino=grafo.h(vecino)
                )
                frontera.ADD(hijo)

    return None