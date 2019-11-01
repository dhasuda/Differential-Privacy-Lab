from sklearn.datasets import load_breast_cancer

class BreastCancerDP:
  instance = None
  class __BreastCancerDPSingleton:
    maxSize = None
    loadedData = None
    def __init__(self, maxSize=None):
      x = 1
      self.maxSize = maxSize

    def getAllData(self):
      if not self.loadedData:
        self.loadedData = load_breast_cancer()
      return self.loadedData.data

    def getAllTargets(self):
      if not self.loadedData:
        self.loadedData = load_breast_cancer()
      return self.loadedData.target

  def __init__(self, maxSize=None):
    if not BreastCancerDP.instance:
      BreastCancerDP.instance = BreastCancerDP.__BreastCancerDPSingleton(maxSize)
    else:
      BreastCancerDP.instance.maxSize = maxSize
    
  def __getattr__(self, name):
    return getattr(self.instance, name)