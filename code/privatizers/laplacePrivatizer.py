import numpy as np
import abstractPrivatizer

class LaplacePrivatizer(abstractPrivatizer.AbstractPrivatizer):
  _mean = 0.0
  _epsilon = 1.0

  def __init__(self, epsilon=1.):
    if (type(epsilon) != float):
      raise ValueError('Not a valid epsilon')
    if (epsilon <= 0.0):
      raise ValueError('Not a valid epsilon')
    self._epsilon = epsilon

  def privatizeSingleAnswer(self, value, sensitivityValue=1.):
    sanitizedTruth = 0
    try:
      sanitizedTruth = float(value)
    except:
      raise ValueError('Not valid value to be privatized')
    sensitivityValue = max(0.00001, sensitivityValue)
    noise = np.random.laplace(self._mean, sensitivityValue / self._epsilon, 1)[0]
    return float(sanitizedTruth + noise)