import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt
import json
# LOCAL IMPORTS
from Airport import Airport
from Node import Node
from Graph import Graph

#CONSTANTS
ORIGIN = 'CCS'
DESTINATION = 'SBH'

# LOADING DATA
def loadAirports():
  '''
  Loads the data from the json in the data folder,
  loops through it and creates airport objects,
  makes the code as the key for the object in a dictionary
  returns the airport dictionary
  '''
  # AIRPORTS
  airportsData = open('./data/airportData.json')
  airports = json.load(airportsData)

  _airports = {}
  # PUTS ELEMENTS INSIDE DICT WITH THE CODE AS THE KEY
  for key in airports:
    _airports[airports[key]['code']] = (Airport(airports[key]['city'], airports[key]['code'], airports[key]['visaRequired']))

  # CLOSES FILE
  airportsData.close()
  return _airports

def loadNodes(airports):
  '''
  Loads the data from the json in the data folder,
  loops through it and creates node objects,
  appends the node objects into an array
  and returns the node array
  '''
  # NODES
  travelData = open('./data/travelData.json')
  travel = json.load(travelData)

  _travel = []
  # PUTS ELEMENTS INSIDE LIST
  for elem in travel['Travels']:
    endAirport = airports[elem['end']]
    _travel.append(Node(elem['start'], elem['end'], elem['cost'], endAirport.visaRequired))

  # CLOSES FILE
  travelData.close()
  return _travel

def makeGraph(nodes, graph, airports, traveler):
  '''
  Takes in a graph object and a list of nodes,
  loops through the nodes
  and creates edges on the graph instance
  '''
  for node in nodes:
    if airports[node.start].visaRequired and traveler.hasVisa:
      graph.addEdge(node.start, node.end, node.cost, airports)

    if not airports[node.start].visaRequired:
      graph.addEdge(node.start, node.end, node.cost, airports)

def plotGraph(graph):
  adjacencyList = {}

  for key, value in graph.items():
    adjacencyList.update({ key: { item[0]: item[1] for item in value } })

  G = nx.Graph(adjacencyList)
  nx.draw_networkx(G, with_labels=True, node_color="c", edge_color="k", font_size=8)

  plt.axis("off")
  plt.show()
  return adjacencyList


def runApp(traveler, origin, destination):
  '''
  Runs the app
  '''
  airports = loadAirports()
  travels = loadNodes(airports)
  # Creating graph object
  graph = Graph()
  # traveler = Traveler('Ricardo', 'Micale', True)
  makeGraph(travels, graph, airports, traveler)
  graph.printData()
  path, totalCost = graph.traverseGraph(origin, destination)
  result = (graph.getPath(destination, origin, path), totalCost)
  for item in range(len(result[0])):
    airport = airports[result[0][item]]
    result[0][item] = f"{airport.code} ({airport.city})"
  plotGraph(graph.graph)
  # print(result)
  return result

