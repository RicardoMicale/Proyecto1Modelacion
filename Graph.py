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
    # print(costMatrix)

    # visited nodes
    visitedAirports = []

    # traverse list
    toVisit = self.graph[origin]
    # print(airports)
    currentAirport = origin
    totalCost = 0

    if origin == destination:
      return ([origin], 0)

    while currentAirport != destination:
      visitedAirports.append(currentAirport)
      costs = []
      nextAirports = []

      for node in toVisit:
        newCost = node[1]
        if costMatrix[node[0]] != float("Inf"):
          oldCost = costMatrix[node[0]]
          if newCost < oldCost:
            costMatrix[node[0]] = newCost

        costs.append(node[1])
        nextAirports.append(node[0])

      if destination in nextAirports:
        visitedAirports.append(destination)
        lastCost = costs[nextAirports.index(destination)]
        totalCost += lastCost
        break

      # gest the minimum cost on the cost array
      minCost = min(costs)

      # if the minimum cost has already been visited
      if nextAirports[costs.index(minCost)] in visitedAirports:
        # removes that cost from the options and looks for the next lower cost
        costs.remove(minCost)
        minCost = min(costs)

      if len(self.graph[nextAirports[costs.index(minCost)]]) == 1:
        possibleAirport = self.graph[nextAirports[costs.index(minCost)]]
        if possibleAirport[0] in visitedAirports:
          costs.remove(minCost)
          minCost = min(costs)

      nextAirport = nextAirports[costs.index(minCost)]
      visitedAirports.append(nextAirport)

      toVisit = self.graph[nextAirport]


    return (visitedAirports, totalCost)

  def printData(self):
    for key in self.graph: print(f'{key} --> {self.graph[key]}')
