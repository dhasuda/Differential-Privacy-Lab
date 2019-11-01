import unittest
import numpy as np
import generalAdapter as adapter

class GeneralAdapterTests(unittest.TestCase):

  def testInitialize(self):
    ad = adapter.GeneralAdapter(10)
    self.assertEqual(10, ad.dimensions)

  def testInvalidInputs(self):
    ad = adapter.GeneralAdapter(10)

    self.assertRaises(ValueError, lambda: ad.fromRaw('a'))
    self.assertRaises(ValueError, lambda: ad.fromRaw([1]))
  
  def testOutputFormat(self):
    ad = adapter.GeneralAdapter(10)

    array = np.ndarray(shape=(2,2), dtype=float, order='F')
    output = ad.fromRaw(array)
    self.assertEqual(list, type(output))
    self.assertEqual(list, type(output[0]))
    self.assertEqual(float, type(output[0][0]))

  def testToIntList(self):
    ad = adapter.GeneralAdapter(10)
    values = 0.1
    self.assertEqual(0, ad.toDiscreteValue(values))

    values = [0.1, 0.5, 0.6, 1.1, -0.1, 1.6, 9.1, 10.0]
    self.assertEqual([0, 0, 1, 1, 0, 2, 9, 9], ad.toDiscreteValue(values))

    ad = adapter.GeneralAdapter(3, 1)
    values = [0.2, 1.3, 3.1, 3.6, -1.2]
    self.assertEqual([1, 1, 3, 3, 1], ad.toDiscreteValue(values))


if __name__ == "__main__":
  unittest.main()