from graph import Graph
from bfs import bfs
from dfs import dfs
from uniform_cost import uniform_cost
from greedy import greedy
from astar import astar


def print_solution(node):
    path = []
    total_cost = node.g

    while node:
        path.append(node.name)
        node = node.parent

    path.reverse()

    print("Camino:", " -> ".join(path))
    print("Costo total:", total_cost)


if __name__ == "__main__":

    graph = Graph("funcion_de_costo.xlsx", "heuristica.xlsx")

    start = "Warm-Up"
    goal = "Stretching"

    print("=== BFS ===")
    print_solution(bfs(graph, start, goal))

    print("\n=== DFS ===")
    print_solution(dfs(graph, start, goal))

    print("\n=== Uniform Cost ===")
    print_solution(uniform_cost(graph, start, goal))

    print("\n=== Greedy ===")
    print_solution(greedy(graph, start, goal))

    print("\n=== A* ===")
    print_solution(astar(graph, start, goal))