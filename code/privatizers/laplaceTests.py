import unittest
import laplacePrivatizer

class LaplacePrivatizerTests(unittest.TestCase):

  def testInitializer(self):
    self.assertRaises(ValueError, lambda:laplacePrivatizer.LaplacePrivatizer('a'))
    self.assertRaises(ValueError, lambda: laplacePrivatizer.LaplacePrivatizer(0.))
    self.assertRaises(ValueError, lambda: laplacePrivatizer.LaplacePrivatizer(-1.))
      
    priv = laplacePrivatizer.LaplacePrivatizer()
    self.assertEqual(1., priv._scale)

    priv = laplacePrivatizer.LaplacePrivatizer(0.5)
    self.assertEqual(0.5, priv._scale)

  def testPrivatizeSingleAnswer(self):
    priv = laplacePrivatizer.LaplacePrivatizer()
    self.assertRaises(ValueError, lambda: priv.privatizeSingleAnswer('a'))
      

    answer = priv.privatizeSingleAnswer(1.0)
    self.assertTrue(type(answer) == float)

  def testPrivatizeList(self):
    priv = laplacePrivatizer.LaplacePrivatizer()

    emptyList = priv.privatize([])
    self.assertEqual([], emptyList)

    notEmptyList = priv.privatize([-1., 0., 1., 2.])
    self.assertEqual(len(notEmptyList), len([-1., 0., 1., 2.]))
    for value in notEmptyList:
      self.assertTrue(type(value) == float)

  def testPrivatize(self):
    priv = laplacePrivatizer.LaplacePrivatizer()

    emptyList = priv.privatize([])
    self.assertEqual([], emptyList)

    notEmptyList = priv.privatize([[-1., 0., 1., 2.], [-1., 0.]])
    self.assertEqual(len(notEmptyList), len([[-1., 0., 1., 2.], [-1., 0.]]))
    for value in notEmptyList:
      self.assertTrue(type(value) == list)

    notEmptyList = priv.privatize([[-1., 0., 1., 2.], [-1., 0.], 1.])
    self.assertEqual(len(notEmptyList), len([[-1., 0., 1., 2.], [-1., 0.], 1.]))
    self.assertTrue(type(notEmptyList[-1]) == float)

if __name__ == "__main__":
  unittest.main()