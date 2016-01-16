
def printBoard(board):
	print(' | ' + board[0]+ ' | ' + board[1]+ ' | ' + board[3] + ' | ' + board[4])

	print(' | ' + board[5]+ ' | ' + board[5]+ ' | ' + board[6] +' | ' + board[7])

	print(' | ' + board[8]+ ' | ' + board[9]+ ' | ' + board[10] +' | ' + board[11])

	print(' | ' + board[12]+ ' | ' + board[13]+ ' | ' + board[14] +' | ' + board[15])

def populate(thing):
	thing = list(thing)
	for i in range(0, 15):
		thing.append('O')

theBoard = ('1','2','3')

populate(theBoard)

printBoard(theBoard)








print('Welcome to battleship!')
