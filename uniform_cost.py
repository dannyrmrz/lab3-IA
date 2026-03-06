from node import Node
from queues import PriorityQueue

def uniform_cost(graph, start, goal):
    frontier = PriorityQueue()
    frontier.ADD(Node(start, g=0))
    explored = set()

    while not frontier.EMPTY():
        current = frontier.POP()

        if current.name == goal:
            return current

        explored.add(current.name)

        for neighbor, cost in graph.neighbors(current.name):
            if neighbor not in explored:
                g = current.g + cost
                frontier.ADD(Node(neighbor, current, g=g))

    return None