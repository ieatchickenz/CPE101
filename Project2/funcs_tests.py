#Alex Petrov

import unittest
from landerFuncs import *
import landerFuncs

class TestCases(unittest.TestCase):

    def test_updateAcceleration(self):
       self.assertAlmostEqual(landerFuncs.updateAcceleration(1.62, 5), 0)
       self.assertAlmostEqual(landerFuncs.updateAcceleration(1.62, 1), -1.296)
       self.assertAlmostEqual(landerFuncs.updateAcceleration(1.62, 9), 1.296)
    
    def test_updateAltitide(self):
       self.assertEqual(landerFuncs.updateAltitude(-1, 4, 3), 0)
       self.assertAlmostEqual(landerFuncs.updateAltitude(1500, -54, -1.62 ), 1445.19)
       self.assertAlmostEqual(landerFuncs.updateAltitude(50, -10, 25), 52.5)
   
    def test_updateFuel(self):
       self.assertEqual(landerFuncs.updateFuel(40, 9), 31)
       self.assertEqual(landerFuncs.updateFuel(500, 1), 499)
       self.assertEqual(landerFuncs.updateFuel(45, 5), 40)
   
    def test_updateVelocity(self):
       self.assertAlmostEqual(landerFuncs.updateVelocity(-54, -1.62), -55.62)
       self.assertAlmostEqual(landerFuncs.updateVelocity(-50, 30), -20)
       self.assertAlmostEqual(landerFuncs.updateVelocity(-90, 0), -90)
 

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

