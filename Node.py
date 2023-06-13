class Node:
  def __init__(self, start, end, cost, visaNeeded):
    self.start = start
    self.end = end
    self.cost = cost
    self.visaNeeded = visaNeeded

  def printData(self):
    print(f'Origin {self.start}, destination: {self.end}, cost: {self.cost}, visa: {self.visaNeeded}')
