class Airport:
  def __init__(self, city, code, visaRequired):
    self.city = city
    self.code = code
    self.visaRequired = visaRequired

  def printData(self):
    print(f'{self.city} airport, code: {self.code}, visa required: {self.visaRequired}')
