import numpy as np

class GeneralAdapter:
  dimensions = 2
  initialVaue = 0
  def __init__(self, dimensions, initialValue = 0):
    self.dimensions = dimensions
    self.initialValue = initialValue

  def fromRaw(self, rawData):
    if (type(rawData) == np.ndarray):
      adaptedData = []
      for data in rawData:
        adaptedData.append(self.fromRaw(data))
      return adaptedData  
    else:
      return self.toFloat(rawData)

  def toFloat(self, value):
    try:
      return float(value)
    except:
      raise ValueError('Cannot parse to float')

  def toDiscreteValue(self, data):
    if type(data) == list:
      intList = []
      for value in data:
        intList.append(self.toDiscreteValue(value))
      return intList
    elif type(data) == float:
      discreteWithZeroMean = round(data - self.initialValue)

      discreteWithinBounds = 0
      if (discreteWithZeroMean >= (self.dimensions-1)):
        discreteWithinBounds = self.dimensions-1
      elif(discreteWithZeroMean <= 0):
        discreteWithinBounds = 0
      else:
        discreteWithinBounds = discreteWithZeroMean % self.dimensions

      discreteValue = discreteWithinBounds + self.initialValue
      return discreteValue
    else:
      raise ValueError('It only accepts lists of float values')