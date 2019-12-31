# Project 3 - Tic-Tac-Toe Simulator
# 
# Name: Alex Petrov
# Instructor: S. Einakian 
# Section: 01
# Functions definitions comes here

import random

#Welcomes player and determines who is playing based on an input.
#None -> int
def Welcome():
   print('Welcome to Tic-Tac-Toe!')
   print('Two people play Tic Tac Toe with paper and pencil. One player is X and the other player is O. Players take')
   print('turns placing their X or O. If a player gets three of their marks on the board in a row, column or one of the')
   print('two diagonals, they win. When the board fills up with neither player winning, the game ends in a draw.')
   print()
   player = int(input('If you are playing against the computer press 1. Otherwise, press 2: '))
   while player != 1 and player != 2:
      print('You must choose 1 or 2.')
      player = int(input('If you are playing against the computer press 1. Otherwise, press 2: '))
   return player

#creates a representation of the board with the postions coresponding to a value. Also creates the board list and returns it.
#None -> list
def createBoard():
   
   print('1','  | ','2',' | ','3')
   print('---------------')
   print('4','  | ','5',' | ','6')
   print('---------------')
   print('7','  | ','8',' | ','9')
   
   board=[' ']*9

   return board


#Takes the board list and prints it in a specifc pattern.
#list -> None
def printBoard(board):
   print()
   print(board[0],'  | ',board[1],' | ',board[2])
   print('---------------')
   print(board[3],'  | ',board[4],' | ',board[5])
   print('---------------')
   print(board[6],'  | ',board[7],' | ',board[8])
   print()
    
#chooses between X and O based on a user input and returns one of the two.
#None -> string
def pickLetter():
   letter = input('Choose X or O: ')

   while letter != 'X' and letter != 'O':
      print('You may only choose between X and O')
      letter = input('Choose X or O: ')
   return letter


#Takes the board and letter currently selected and appends the letter into the board list based on the inputed index. Returns the updated board.
#int list -> list
def getInput(letter, board):
   p = int(input("Where would you like to place your letter (pick in range of 1-9): "))
   
   while True:
      #pos = p-1
      if p < 1 or p > 9:
         print('Invalid move! The location must be between 1 and 9. Please try again.')
         p = int(input("Where would you like to place your letter (pick in range of 1-9): "))
      else:
         if board[p-1] != ' ':
            print('Invalid move! Location is already taken. Please try again.')
            p = int(input("Where would you like to place your letter (pick in range of 1-9): "))
            #pos = p-1
         else:
            board[p-1] = letter
            break
   return board

#Takes the board and letter currently selected and appends the letter into the board list based on a random index chosen by the random functionality. Returns the updated board.
#int list -> list
def getComputerInput(letter, board):
   p = random.randint(0,9) 
   print("Where would you like to place your letter (pick in range of 1-9): ", p)
   
   while True:
      if p < 1 or p > 9:
         print('Invalid move! The location must be between 1 and 9. Please try again.')
         p = random.randint(0,9)
         print("Where would you like to place your letter (pick in range of 1-9): ", p)
      else:
         if board[p-1] != ' ':
            print('Invalid move! Location is already taken. Please try again.')
            p = random.randint(0,9)
            print("Where would you like to place your letter (pick in range of 1-9): ", p)
         else:
            board[p-1] = letter
            break
   return board



#takes the updated board list and checks if the rows have 3 matching characters. Returns True or False.
#list -> bool
def checkRows(board):
   if board[0] == board [1] == board[2] != ' ':
      return True 
   elif board[3] == board [4] == board[5] != ' ':
      return True
   elif board[6] == board [7] == board[8] != ' ':
      return True

#takes the updated board list and checks if the columns have 3 matching characters. Returns True or False.
#list -> bool
def checkCols(board):
   if board[0] == board [3] == board[6] != ' ':
      return True
   elif board[1] == board [4] == board[7] != ' ':
      return True
   elif board[2] == board [5] == board[8] != ' ':
      return True
   
#takes the updated board list and checks if the diagnals have 3 matching characters. Returns True or False.
#list -> bool
def checkDiags(board):
   if board[0] == board [4] == board[8] != ' ':
      return True
   elif board[2] == board [4] == board[6] != ' ':
      return True
  
   
#takes the updated board and checks if any of the check Funcs are True
#list -> bool
def checkWin(board):
   if checkRows(board) == True:
      return True 
   elif checkCols(board) == True:
      return True
   elif checkDiags(board) == True:
      return True
   else:
      return False
#takes the updated board list and checks if there are any open spaces. Returns True or False.
#list -> bool
def boardFull(board):
   for s in board:
      if s == ' ':
         return False 
   return True
   
#takes the number turns that have passed, adds one, and returns the new nmber of turns
#int -> int 
def turnCount(turn):
   if turn < 9:
      turn += 1
      return turn 

