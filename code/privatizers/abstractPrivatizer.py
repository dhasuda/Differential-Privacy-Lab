from abc import ABC, abstractmethod

class AbstractPrivatizer(ABC):
  def privatize(self, data, sensitivityValue=0.001, sensitivityList = None):
    if (type(data) == list):
      if (len(data) == 0):
        return []
      privatizedData = []
      sensitivity = sensitivityValue
 
      if (type(data[0]) == list and sensitivityList == None):
        sensitivityList = self.getSensitivityList(data)

      counter = 0
      for value in data:
        if (type(value) == list):
          sensitivity = sensitivityList
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
    
  def getSensitivityList(self, dataList):
    sensitivityGeneratedList = []
    for i in range(len(dataList[0])):
      column = [row[i] for row in dataList]
      singleSensitivityValue = abs(max(column) - min(column))
      sensitivityGeneratedList.append(singleSensitivityValue)
    return sensitivityGeneratedList

    
  @abstractmethod
  def privatizeSingleAnswer(self, value, sensitivityValue):
    pass
    