class Nodo:
    def __init__(self, estado, padre=None, accion=None, costoCamino=0):
        self.Estado = estado              # ID del estado
        self.Padre = padre                # Nodo padre
        self.Accion = accion              # Acción aplicada
        self.CostoCamino = costoCamino    # g(n)

    def __lt__(self, other):
        return self.CostoCamino < other.CostoCamino