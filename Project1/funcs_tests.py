#Project 1
# 
# Name: Alex Petrov
# Instructor: S. Einakian 
# Section: 01

import unittest
from funcs import *

class TestCases(unittest.TestCase):
          
   def test_poundsToKG1(self):
       self.assertAlmostEqual(poundsToKG(100), 45.3592)
       self.assertAlmostEqual(poundsToKG(1300), 589.6696)
       self.assertAlmostEqual(poundsToKG(50), 22.6796)
       self.assertAlmostEqual(poundsToKG(500), 226.796)
    
   def test_getMassObject(self):
       self.assertEqual(getMassObject('t'), 0.1) 
       self.assertEqual(getMassObject('g'), 5.3)
       self.assertEqual(getMassObject(9), 0.0)
       self.assertEqual(getMassObject('p'), 1.0)
       self.assertEqual(getMassObject('r'), 3.0)
       self.assertEqual(getMassObject('l'), 9.07)

   def test_getVelocityObject(self):
       self.assertAlmostEqual(getVelocityObject(100), 22.135943621178658)
       self.assertAlmostEqual(getVelocityObject(50), 15.652475842498529)
       self.assertAlmostEqual(getVelocityObject(1500), 85.73214099741124)
       self.assertAlmostEqual(getVelocityObject(500), 49.49747468305833)

   def test_getVelocitySkater(self):
       self.assertAlmostEqual(getVelocitySkater(100, 100, 100,), 100)
       self.assertAlmostEqual(getVelocitySkater(22.7696 , 5.3, 20), 4.655329913568969)
       self.assertAlmostEqual(getVelocitySkater(55, 0.1, 50), 0.09090909090909091)
       self.assertAlmostEqual(getVelocitySkater(90, 3.0, 45), 1.5)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
