class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def getWeight(self):
        return self.weight

    def __str__(self):
        return str(self.getStart) + "." + str(self.getEnd)

    __repr__ = __str__


class dGraph:
    def __init__(self, n):
        self.vertices = n
        self.graph = [[] for i in range(self.vertices)]

    def addEdge(self, start, end, weight):
        edge = Edge(start, end, weight)
        self.graph[start].append(edge)


if __name__ == "__main__":
    graph = dGraph(5)
    graph.addEdge(0, 1, 35)
    print(graph.graph)