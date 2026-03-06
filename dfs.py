from node import Nodo
from estructuras import PilaLIFO


def DFS(graph, start, goal):

    frontier = PilaLIFO()
    frontier.ADD(Nodo(estado=start, padre=None, accion=None, costoCamino=0))

    explored = set()

    while not frontier.EMPTY():

        current = frontier.POP()

        if current.Estado == goal:
            return current

        explored.add(current.Estado)

        for neighbor, cost in graph.vecinos(current.Estado):

            if neighbor not in explored:

                child = Nodo(
                    estado=neighbor,
                    padre=current,
                    accion=neighbor,
                    costoCamino=current.CostoCamino + cost
                )

                frontier.ADD(child)

    return None