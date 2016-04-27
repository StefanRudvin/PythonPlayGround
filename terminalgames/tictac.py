import random
import os

def drawBoard(board):

	print(' | |')

	print(' '+board[7]+'|'+board[8]+'|'+board[9])

	print(' | |')

	print(' '+board[4]+'|'+board[5]+'|'+board[6])

	print(' | |')

	print(' '+board[1]+'|'+board[2]+'|'+board[3])

def inputPlayerLetter():
	#returns the order with an array, X or O in order
	letter = ''
	while not(letter == 'X' or letter == 'O'):
		print('Do you want to be X or O?')
		letter = input().upper()

		if letter == 'X':
			return ['X', 'O']
		else: 
			return ['O', 'X']

def whoGoesFirst():
	#Randomly chooses who goes first
	if random.randint(0,1) == 0:
		return 'computer'
	else:
		return 'player'

def playAgain():
	#returns true or false depending on whether input starts with yes or not
	print('Do you want to play again? (Yes or no)')
	return input().lower().startswith('y')

def makeMove(board, letter, move):
	board[move] = letter


def isWinner(bo,le):
	#returns true if player has won
	#bo = board le= letter for less writing
	return ((bo[7]==le and bo[8]==le and bo[9]==le) or #across the top
		(bo[3]==le and bo[6]==le and bo[9]==le) or #Right
		(bo[1]==le and bo[4]==le and bo[7]==le) or #Left
		(bo[8]==le and bo[2]==le and bo[5]==le) or #Middle
		(bo[1]==le and bo[2]==le and bo[3]==le) or #across bottom
		(bo[4]==le and bo[5]==le and bo[6]==le) or #across middle
		(bo[1]==le and bo[5]==le and bo[9]==le) or #Diagonal #1
		(bo[3]==le and bo[5]==le and bo[7]==le) or #Diagonal #2)

def getBoardCopy(board):
	#make a duplicate of the board list and return the duplicate
	dupeBoard = []

	for i in board:
		dupeBoard.append(i)

def isSpaceFree(board, move):
	#return true if move if free on board
	return board[move]==''

def getPlayerMove(board):
	#let the player type in move
	move = ''
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
		print ('What is your next move? (1-9)')
		move = input()
	return int(move)

def chooseRandomMoveFromList(board, movesList):
	#returns a valid move from the passed list on the passed board.
	#returns none if there is no valid move.
	possibleMoves = []
	for i in movesList:
		if isSpaceFree(board, i):
			possibleMoves.append(i)
	if len(possibleMoves) != 0:
		return random.choice(possibleMoves)
	else:
		return None

def getComputerMove(board, computerLetter):
	#Given a board and the computer's letter, determine where to move and return that move.
	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

		#computer AI
		#Check if we can win next move
	for i in range(1,10):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy,computerLetter,i)
			if isWinner(copy,computerLetter):
				return i

	for i in range(1,10):
		copy = getBoardCopy(board)
		if isSpaceFree(copy,i):
			makeMove(copy,playerLetter,i)
			if isWinner(copy,playerLetter):
				return i

	#Try to take one of the corners, if they are free
	move = chooseRandomMoveFromList(board,[1,3,7,9])
	if move != None:
		return move

	#Try to take center if it's free
	if isSpaceFree(board, 5):
		return 5

	#Move on one of the sides
	return chooseRandomMoveFromList(board, [2,4,6,8])

	def isBoardFull(board):
		# return true if every space is taken. Otherwise return False
		for i in range(1,10):
			if isSpaceFree(board, i):
				return False
		return True



print('Welcome to Tic Tac Toe!')

while True:
	#Reset board
	theBoard = ['']*10
	playerLetter,computerLetter = inputPlayerLetter()
	turn = whoGoesFirst()

	while gameIsPlaying:
		if turn == 'player':
			#Player's turn
			drawBoard(theBoard)
			makeMove(theBoard,playerLetter,move)

			if isWinner(theBoard,playerLetter):
				drawBoard(theBoard)
				print('Congratulations! You won the game!')
				gameIsPlaying = False
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('The game is a tie!')
					break
				else:
					turn = 'computer'
		else:
			#Computer's turn
			move = getComputerMove(theBoard, computerLetter)
			makeMove(theBoard,computerLetter,move)

			if isWinner(theBoard,computerLetter):
				drawBoard(theBoard)
				print('You lost the game!')
				gameIsPlaying = False
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('The game is a tie!')
					break
				else:
					turn = 'player'
	if not playAgain():
		break













	