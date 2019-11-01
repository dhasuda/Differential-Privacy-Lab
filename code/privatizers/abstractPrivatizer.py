from abc import ABC, abstractmethod

class AbstractPrivatizer(ABC):
  def privatize(self, data, sensitivityValue=0.001, sensitivityList = None):
    if (type(data) == list):
      if (len(data) == 0):
        return []
      privatizedData = []
      counter = 0
      sensitivity = sensitivityValue

      sensitivityGeneratedList = []
      if (type(data[0]) == list and sensitivityList == None):
          for i in range(len(data[0])):
            column = [row[i] for row in data]
            singleSensitivityValue = abs(max(column) - min(column))
            sensitivityGeneratedList.append(singleSensitivityValue)
      elif (sensitivityList != None):
        sensitivityGeneratedList = sensitivityList

      for value in data:
        if (type(value) == list):
          sensitivity = sensitivityGeneratedList
        else:
          if (type(sensitivityValue) == float):
            sensitivity = sensitivityValue
          else:
            sensitivity = sensitivityValue[counter]

        privatizedData.append(self.privatize(value, sensitivity))
        counter += 1
      
      return privatizedData

    else:
      return self.privatizeSingleAnswer(data, sensitivityValue)
    
  @abstractmethod
  def privatizeSingleAnswer(self, value, sensitivityValue):
    pass
    