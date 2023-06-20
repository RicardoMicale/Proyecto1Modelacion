class Traveler:
  def __init__(self, firstName, lastName, hasVisa):
    self.firstName = firstName
    self.lastName = lastName
    self.hasVisa = hasVisa

  def printData(self):
    print(f"{self.firstName} {self.lastName}, visa: {'Si' if self.hasVisa else 'No'}")
