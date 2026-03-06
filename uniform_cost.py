from node import Nodo
from estructuras import ColaPrioridad

def CostoUniforme(grafo, inicio, meta):

    frontera = ColaPrioridad()
    frontera.ADD(Nodo(inicio, costoCamino=0))
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