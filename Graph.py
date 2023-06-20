import heapq as heap

class Graph:
  def __init__(self):
    self.graph = dict()
    self.vertices = len(self.graph)

  def addEdge(self, start, end, cost, airports):
    # If the node is not in the graph
    # it creates a sublist under the key
    if start not in self.graph: self.graph[start] = []
    if end not in self.graph: self.graph[end] = []

    # appends a tuple with the destination, cost and requirement for a visa
    self.graph[start].append((end, float(cost), airports[end].visaRequired))
    self.graph[end].append((start, float(cost), airports[start].visaRequired))
    return self.graph

  def traverseGraph(self, origin, destination):
    costMatrix = {}
    for vertex in self.graph.keys():
      costMatrix[vertex] = float("Inf") if vertex != origin else 0

    queue = []
    heap.heappush(queue, (0, origin))

    # visited nodes
    visitedAirports = []
    # path taken to destination
    path = {}

    if origin == destination:
      return ([origin], 0)

    while queue:
      _, node = heap.heappop(queue)
      visitedAirports.append(node)

      for item in self.graph[node]:
        airport = item[0]
        cost = item[1]

        if airport in visitedAirports: continue

        newCost = costMatrix[node] + cost
        if costMatrix[airport] > newCost:
          path[airport] = node
          costMatrix[airport] = newCost
          heap.heappush(queue, (newCost, airport))

    return (path, costMatrix[destination])

  def getPath(self, destination, origin, path):
    travel = []
    currentNode = destination
    while currentNode != origin:
      travel.append(currentNode)
      prevNode = currentNode
      currentNode = path[prevNode]

    travel.append(origin)
    return travel[::-1]


  def printData(self):
    for key in self.graph: print(f'{key} --> {self.graph[key]}')
