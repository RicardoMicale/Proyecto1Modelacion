import json
# LOCAL IMPORTS
from Airport import Airport
from Node import Node
from Traveler import Traveler
from Graph import Graph

# LOADING DATA
def loadAirports():
  '''
  Loads the data from the json in the data folder
  Loops through it and creates airport objects
  Makes the code as the key for the object in a dictionary
  Returns the airport dictionary
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
  Loads the data from the json in the data folder
  Loops through it and creates node objects
  Appends the node objects into an array
  Returns the node array
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

def runApp():
  '''
  Runs the app
  '''
  airports = loadAirports()
  travels = loadNodes(airports)

  #for i in travels: i.printData()
