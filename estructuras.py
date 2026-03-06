import heapq

class ColaFIFO:
    def __init__(self):
        self.lista = []

    def EMPTY(self):
        return len(self.lista) == 0

    def TOP(self):
        return self.lista[0]

    def POP(self):
        return self.lista.pop(0)

    def ADD(self, elemento):
        self.lista.append(elemento)


class PilaLIFO:
    def __init__(self):
        self.lista = []

    def EMPTY(self):
        return len(self.lista) == 0

    def TOP(self):
        return self.lista[-1]

    def POP(self):
        return self.lista.pop()

    def ADD(self, elemento):
        self.lista.append(elemento)


class ColaPrioridad:
    def __init__(self):
        self.lista = []

    def EMPTY(self):
        return len(self.lista) == 0

    def TOP(self):
        return self.lista[0]

    def POP(self):
        return heapq.heappop(self.lista)

    def ADD(self, elemento):
        heapq.heappush(self.lista, elemento)