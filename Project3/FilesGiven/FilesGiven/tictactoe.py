# Project 3 - Tic-Tac-Toe Simulator
# 
# Name: Alex Petrov
# Instructor: S. Einakian 
# Section: 01
#Main Program

from tictactoeFuncs import *

player = Welcome()
#This is against another person
if player == 2:
	#create board
	board = createBoard()
	print('These are the numbers coressponding to the spaces you can play.')
	print('This is what your board looks like now.')
	printBoard(board)
	print('Player 1 choose your letter!')
	letter = pickLetter()
	print('Player 2 you have the other letter.')
	turn = 0
	while turn < 9:
		print()
		print(letter, "it is your turn!")
		board = getInput(letter, board)
		printBoard(board)
		checkRows(board)
		checkCols(board)
		checkDiags(board)
		turn = turnCount(turn)
		win = checkWin(board)
		if win == True:
			print('Player',letter,'is the winner')
			break
		full = boardFull(board)
		if full == True:
			print("It's a tie! Everyone is a winner.")
	
		if letter == 'X':
			letter = 'O'
		else:
			letter = 'X'

#This is against a computer
else:
	board = createBoard()
	print('These are the numbers coressponding to the spaces you can play.')
	print('This is what your board looks like now.')
	printBoard(board)
	print('Player 1 choose your letter!')
	player1 = letter = pickLetter()
	print('The computer has the other letter.')
	turn = 0
	while turn < 9:
		print()
		print(letter, "it is your turn!")
		if letter != player1:
			board = getComputerInput(letter, board)
		else:
			board = getInput(letter, board)

		printBoard(board)
		checkRows(board)
		checkCols(board)
		checkDiags(board)
		turn = turnCount(turn)
		win = checkWin(board)
		if win == True:
			print('Player',letter,'is the winner')
			break
		full = boardFull(board)
		if full == True:
			print("It's a tie! Everyone is a winner.")
	
		if letter == 'X':
			letter = 'O'
		else:
			letter = 'X'











