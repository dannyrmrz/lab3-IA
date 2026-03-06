import pandas as pd

class Grafo:
    def __init__(self, archivo_costos, archivo_heuristica):

        matriz = pd.read_excel(archivo_costos, index_col=0)

        self.aristas = {}

        for origen in matriz.index:
            self.aristas[origen] = []
            for destino in matriz.columns:
                costo = matriz.loc[origen, destino]
                if pd.notna(costo) and costo > 0:
                    self.aristas[origen].append((destino, costo))

        heuristica_df = pd.read_excel(archivo_heuristica)

        self.heuristica = dict(
            zip(heuristica_df.iloc[:,0], heuristica_df.iloc[:,1])
        )

    def vecinos(self, estado):
        return self.aristas.get(estado, [])

    def h(self, estado):
        return self.heuristica.get(estado, 0)