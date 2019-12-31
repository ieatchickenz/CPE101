
# Project 3 - Tic-Tac-Toe Simulator
# 
# Name: Alex Petrov
# Instructor: S. Einakian 
# Section: 01

import unittest
from tictactoeFuncs import *

class TestCases(unittest.TestCase):
   def test_checkRow(self):
   	  testboard = [' ']*9
   	  testboard1 = ['X']*9
   	  testboard2 = ['O']*9
   	  testboard3 = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
   	  testboard4 = ['X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O']
   	  self.assertFalse(checkRows(testboard))
   	  self.assertTrue(checkRows(testboard1))
   	  self.assertTrue(checkRows(testboard2))
   	  self.assertFalse(checkRows(testboard3))
   	  self.assertTrue(checkRows(testboard4))

   def test_checkCols(self):
   	   testboard = [' ']*9
   	   testboard1 = ['X']*9
   	   testboard2 = ['O']*9
   	   testboard3 = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
   	   testboard4 = ['X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O']
   	   self.assertFalse(checkCols(testboard))
   	   self.assertTrue(checkCols(testboard1))
   	   self.assertTrue(checkCols(testboard2))
   	   self.assertFalse(checkCols(testboard3))
   	   self.assertFalse(checkCols(testboard4))
   
   def test_checkDiags(self):
   	   testboard = [' ']*9
   	   testboard1 = ['X']*9
   	   testboard2 = ['O']*9
   	   testboard3 = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
   	   testboard4 = ['X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O']
   	   self.assertFalse(checkDiags(testboard))
   	   self.assertTrue(checkDiags(testboard1))
   	   self.assertTrue(checkDiags(testboard2))
   	   self.assertTrue(checkDiags(testboard3))
   	   self.assertFalse(checkDiags(testboard4))

   def test_checkWin(self):
   	   testboard = [' ']*9
   	   testboard1 = ['X']*9
   	   testboard2 = ['O']*9
   	   testboard3 = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
   	   testboard4 = ['X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O']
   	   self.assertFalse(checkWin(testboard))
   	   self.assertTrue(checkWin(testboard1))
   	   self.assertTrue(checkWin(testboard2))
   	   self.assertTrue(checkWin(testboard3))

   def test_fullBoard(self):
   	   testboard = [' ']*9
   	   testboard1 = ['X']*9
   	   testboard2 = ['O']*9
   	   testboard3 = ['X', 'O', 'X', 'O', 'X', 'O', 'X', ' ', 'X']
   	   testboard4 = ['X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O']
   	   self.assertFalse(boardFull(testboard))
   	   self.assertTrue(boardFull(testboard1))
   	   self.assertTrue(boardFull(testboard2))
   	   self.assertFalse(boardFull(testboard3))

   def test_turnCount(self):
   	   self.assertEqual(turnCount(3), 4)
   	   self.assertEqual(turnCount(5), 6)
   	   self.assertEqual(turnCount(6), 7)
   	   self.assertEqual(turnCount(8), 9)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

