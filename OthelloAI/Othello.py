
import random
import sys

def drawBoard(board):
    #This function prints out the board that it was passed. Returns None.
    # HLINE = in between VLINE = all the shit
    HLINE = '  +---+---+---+---+---+---+---+---+'
    VLINE = '  |   |   |   |   |   |   |   |   |'

    print('    1   2   3   4   5   6   7   8')
    print(HLINE)
    for y in range(8):
        print(VLINE)
        print(y+1, end=' ')
        for x in range(8):
            print('| %s' % (board[x][y]), end=' ')
        print('|')
        print(VLINE)
        print(HLINE)

def resetBoard(board):
    #Blanks out the board it is bassed, except for starting position
    for x in range(8):
        for y in range(8):
            board[x][y] = ' '

    #Starting Places
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

def getNewBoard():
    #Creates a new, blank board data structure.
    board= []
    for i in range(8):
        board.append(['']*8)

    return board



def isValidMove(board,tile,xstart,ystart):
    #return false if player's move on space xstart, ystart is invalid
    #If it is a valid move, return a list of spaces that would become players makeMove

    if board[xstart][ystart] != '' or not isOnBoard(xstart,ystart):
        return False

    board[xstart][ystart] = tile #temporarily set tile on board

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x,y = xstart,ystart
        x += xdirection #first step in the direction
        y += ydirection #first step in the direction
        if isOnBoard(x,y) and board[x][y] == otherTile:
            #There is a piece belonging to the player next to our piece
            x += xdirection
            y += ydirection
            if not isOnBoard(x,y):
                continue
            while board[x][y] == otherTile:
                x += xdirection
                y += ydirection
            if not isOnBoard(x,y): #Break out of while loop, then continue
                break
            if not isOnBoard(x,y):
                continue
            if board[x][y] == tile:
                #There are pieces to flip over. Go in the reverse direction until we reach the original space, nothing all the tiles along the way
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
            tilesToFlip.append([x,y])
    board[xstart][ystart] = '' #restore empty spaces
    if len(tilesToFlip) == 0:
        return False
    return tilesToFlip

def isOnBoard(x,y):
    #True if coordinates are on board
    return x >= 0 and x <=7 and y >= 0 and y <= 7

def getBoardWithValidMoves(board,tile):
    #return a new board with marking the valid moves the given player can makeMove

    dupeBoard = getBoardCopy(board)

    for x,y in getValidMoves(dupeBoard,tile):
        dupeBoard[x][y] = ''
    return dupeBoard

def getValidMoves(board,tile):
    #return list of [x,y] lists of valid moves
    validMoves = []

    for x in rangegge(8):
        for y in range(8):
            if isValidMove(board,tile,x,y) != False:
                validMoves.append([x,y])
    return validMoves

def getScoreOfBoard(board):
    #Determine the scoe by counting tiles. Return dict with keys
    xscore = 0
    oscore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X':xscore, 'O':oscore}

def enterPlayerTile():
    #Lets the player type which tile they want to be
    #Return list of players tile as first item, computers as second
    tile = ''
    while not(tile == 'X' or tile == 'O'):
        print('Do you want to be X or O?')
        tile = input().upper()

    #the first element in the list is the players tile, second is computers

    if tile == 'X':
        return ['X','O']
    else:
        return ['O','X']

def whoGoesFirst():
    #Randomly choose the player who goes first
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    #This function returns True if player wants to play again
    print('Do you want to play again?')
    return input().lower().startswith('y')

def makeMove(board, tile, xstart, ystart):
    #Place tile on board at xstart, ystart, and flip and pieces.
    #Return false if its an invalid move, true if valid
    tilesToFlip = isValidMove(board,tile,xstart,ystart)

    if tilesToFlip == False:
        return False

    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True

def getBoardCopy(board):
    #Make a duplicate of board list and return the duplicate
    dupeBoard = getNewBoard()

    for x in range(8):
        for y in range(8):
            dupeBoard[x][y] = board[x][y]

    return dupeBoard

def isOnCorner(x,y):
    #Return true if position is in one of four corners
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)

def getPlayerMove(board, playerTile):
    #Let the player type in their move:
    #Returns the move as [x,y] or returns the strings 'hints' or quit

    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Enter your move or quit or hint')
        move = input().lower()
        if move == 'quit':
            return 'quit'
        if move == 'hints':
            return 'hints'

        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board,playerTile,x,y) == False:
                continue
            else:
                break
        else:
            print('Invalid move. Type x digit (1-8) and y digit (1-8)')
            print('E.g. 81 will be in the top right corner')

    return [x,y]

def getComputerMove(board,computerTile):
    #Given a board and the computer's tile, determine where to move and return that move as a [x,y] list
    possibleMoves = getValidMoves(board,computerTile)

    #Randomize the order of the possible moves
    random.shuffle(possibleMoves)

    #Always go for corner if available
    for x,y in possibleMoves:
        if isOnCorner(x,y):
            return [x,y]

    #Go through all possible moves and remember best move
    bestScore = -1
    for x,y in possibleMoves:
        dupeBoard = getBoardCopy(board)
        makeMove(dupeBoard,computerTile,x,y)
        score = getScoreOfBoard(dupeBoard)[computerTile]
        if score > bestScore:
            bestMove = [x,y]
            bestScore = score
    return bestMove

def showPoints(playerTile,computerTile):
    #Print out currect score
    scores = getScoreOfBoard(mainBoard)
    print('You have %s points. The computer has %s points' %(scores[playerTile], scores[computerTile]))

print('Welcome to Reversi!')
print('Code from: https://inventwithpython.com/chapter15.html')

while True:
    #Reset the board and game
    mainBoard = getNewBoard()
    resetBoard(mainBoard)
    playerTile,computerTile = enterPlayerTile()
    showHints = False
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')

    while True:
        if turn == 'player':
            #Player's turn
            if showHints:
                validMovesBoard = getBoardWithValidMoves(mainBoard,playerTile)
                drawBoard(validMovesBoard)
            else:
                drawBoard(mainBoard)
            showPoints(playerTile,computerTile)
            move = getPlayerMove(mainBoard,playerTile)
            if move == 'quit':
                print('Thanks for playing!')
                sys.exit()
            elif move == 'hints':
                showHints = not showHints
                continue
            else:
                makeMove(mainBoard,playerTile,move[0],move[1])

            if getValidMoves(mainBoard,computerTile) == []:
                break
            else:
                turn = 'computer'
        else:
            #Computer's turn
            drawBoard(mainBoard)
            showPoints(playerTile,computerTile)
            input('Press Enter to see the computers move.')
            x,y = getComputerMove(mainBoard,computerTile)
            makeMove(mainBoard,computerTile,x,y)

            if getValidMoves(mainBoard,playerTile) == []:
                break
            else:
                turn = 'player'
    #Display final score
    drawBoard(mainBoard)
    scores = getScoreOfBoard(mainBoard)
    print('X scored %s points. O scored %s points.' % (scores['X'],scores['O']))
    if scores[playerTile] > scores[computerTile]:
        print('You beat the computer by %s points! Congratulations!' % (scores[playerTile] - scores[computerTile]))
    elif scores[playerTile] < scores[computerTile]:
        print('The computer beat you by %s points! Congratulations you suck!' % (scores[computerTile] - scores[playerTile]))
    else:
        print('The game was tie!')

    if not playAgain():
        break
