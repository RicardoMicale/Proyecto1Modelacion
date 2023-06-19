import json
# LOCAL IMPORTS
from Airport import Airport
from Node import Node
from Traveler import Traveler
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


def runApp():
  '''
  Runs the app
  '''
  airports = loadAirports()
  travels = loadNodes(airports)
  origin = ORIGIN
  destination = DESTINATION
  # Creating graph object
  graph = Graph()
  traveler = Traveler('Ricardo', 'Micale', False)
  makeGraph(travels, graph, airports, traveler)
  #graph.printData()
  path = graph.traverseGraph(origin, destination)
  # print(path)
  #for i in travels: i.printData()

runApp()
