import pandas as pd

class Graph:
    def __init__(self, cost_file, heuristic_file):

        # Leer matriz de costos
        cost_df = pd.read_excel(cost_file, index_col=0)

        self.edges = {}

        for origin in cost_df.index:
            self.edges[origin] = []
            for destination in cost_df.columns:
                cost = cost_df.loc[origin, destination]
                if pd.notna(cost) and cost > 0:
                    self.edges[origin].append((destination, cost))

        # Leer heurística
        heuristic_df = pd.read_excel(heuristic_file)

        self.heuristic = dict(
            zip(heuristic_df.iloc[:,0], heuristic_df.iloc[:,1])
        )

    def neighbors(self, node):
        return self.edges.get(node, [])

    def h(self, node):
        return self.heuristic.get(node, 0)