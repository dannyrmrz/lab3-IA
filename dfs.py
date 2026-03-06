from node import Node
from queues import LIFOQueue

def dfs(graph, start, goal):
    frontier = LIFOQueue()
    frontier.ADD(Node(start))
    explored = set()

    while not frontier.EMPTY():
        current = frontier.POP()

        if current.name == goal:
            return current

        explored.add(current.name)

        for neighbor, cost in graph.neighbors(current.name):
            if neighbor not in explored:
                frontier.ADD(Node(neighbor, current))

    return None