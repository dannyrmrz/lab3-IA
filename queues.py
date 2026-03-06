import heapq

class FIFOQueue:
    def __init__(self):
        self.data = []

    def EMPTY(self):
        return len(self.data) == 0

    def ADD(self, item):
        self.data.append(item)

    def POP(self):
        return self.data.pop(0)


class LIFOQueue:
    def __init__(self):
        self.data = []

    def EMPTY(self):
        return len(self.data) == 0

    def ADD(self, item):
        self.data.append(item)

    def POP(self):
        return self.data.pop()


class PriorityQueue:
    def __init__(self):
        self.data = []

    def EMPTY(self):
        return len(self.data) == 0

    def ADD(self, item):
        heapq.heappush(self.data, item)

    def POP(self):
        return heapq.heappop(self.data)