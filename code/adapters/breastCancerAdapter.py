import numpy as np

def fromRaw(rawData):
  if (type(rawData) != np.ndarray):
    raise ValueError('Raw data must be a numpy ndarray')

  adaptedData = []
  for data in rawData:
    floatList = []
    if (type(data) == np.ndarray):
      for value in data:
        floatList.append(float(value))
      adaptedData.append(list(floatList))
    else:
      adaptedData.append(toFloat(data))

  return adaptedData

def toFloat(value):
  try:
    return float(value)
  except:
    raise ValueError('Cannot parse to float')

def toBinaryInt(data):
  if type(data) == list:
    intList = []
    for value in data:
      intList.append(toBinaryInt(value))
    return intList
  elif type(data) == float:
    if (data >= 0.5):
      return 1
    return 0
  else:
    raise ValueError('It only accepts lists of float values')