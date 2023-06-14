class Graph:
  def __init__(self):
    self.graph = dict()

  def addEdge(self, start, end, cost, airports):
    # If the node is not in the graph
    # it creates a sublist under the key
    if start not in self.graph: self.graph[start] = []
    if end not in self.graph: self.graph[end] = []

    # appends a tuple with the destination, cost and requirement for a visa
    self.graph[start].append((end, float(cost), airports[end].visaRequired))
    self.graph[end].append((start, float(cost), airports[start].visaRequired))
    return self.graph

  def printData(self):
    for key in self.graph: print(f'{key} --> {self.graph[key]}')
