from node import Node
from queues import PriorityQueue

def greedy(graph, start, goal):
    frontier = PriorityQueue()
    frontier.ADD(Node(start, h=graph.h(start)))
    explored = set()

    while not frontier.EMPTY():
        current = frontier.POP()

        if current.name == goal:
            return current

        explored.add(current.name)

        for neighbor, cost in graph.neighbors(current.name):
            if neighbor not in explored:
                frontier.ADD(
                    Node(neighbor, current, h=graph.h(neighbor))
                )

    return None