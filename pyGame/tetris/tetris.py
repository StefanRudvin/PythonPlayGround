"""Tetris."""
import pygame
import sys
import random
import time
from pygame.locals import *  # NOQA

FPS = 25
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BOXSIZE = 20
BOARDWIDTH = 10
BOARDHEIGHT = 20
BLANK = '.'

MOVESIDEWAYSFREQ = 0.15
MOVEDOWNFREQ = 0.1

XMARGIN = int((WINDOWWIDTH-BOARDWIDTH*BOXSIZE)/2)
TOPMARGIN = WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE) - 5

#               R    G    B
WHITE = (255, 255, 255)
GRAY = (185, 185, 185)
BLACK = (0,   0,   0)
RED = (155,   0,   0)
LIGHTRED = (175,  20,  20)
GREEN = (0, 155,   0)
LIGHTGREEN = (20, 175,  20)
BLUE = (0,   0, 155)
LIGHTBLUE = (20,  20, 175)
YELLOW = (155, 155,   0)
LIGHTYELLOW = (175, 175,  20)

BORDERCOLOR = BLUE
BGCOLOR = BLACK
TEXTCOLOR = WHITE
TEXTSHADOWCOLOR = GRAY
COLORS = (BLUE, GREEN, RED, YELLOW)
LIGHTCOLORS = (LIGHTBLUE, LIGHTGREEN, LIGHTRED, LIGHTYELLOW)
assert len(COLORS) == len(LIGHTCOLORS)  # Each color must have light colour

TEMPLATEWIDTH = 5
TEMPLATEHEIGHT = 5

S_SHAPE_TEMPLATE = [['.....',
                  '.....',
                  '..OO.',
                  '.OO..',
                  '.....'],  # NOQA
                 ['.....',  # NOQA
                  '..O..',
                  '..OO.',
                  '...O.',
                  '.....']]

Z_SHAPE_TEMPLATE = [['.....',
                  '.....',
                  '.OO..',
                  '..OO.',
                  '.....'],  # NOQA
                 ['.....',  # NOQA
                  '..O..',
                  '.OO..',
                  '.O...',
                  '.....']]

I_SHAPE_TEMPLATE = [['..O..',
                  '..O..',
                  '..O..',
                  '..O..',
                  '.....'],  # NOQA
                 ['.....',  # NOQA
                  '.....',
                  'OOOO.',
                  '.....',
                  '.....']]

O_SHAPE_TEMPLATE = [['.....',
                  '.....',
                  '.OO..',
                  '.OO..',
                  '.....']]  # NOQA

J_SHAPE_TEMPLATE = [['.....',
                  '.O...',
                  '.OOO.',
                  '.....',
                  '.....'],  # NOQA
                 ['.....',
                  '..OO.',
                  '..O..',
                  '..O..',
                  '.....'],
                 ['.....',
                  '.....',
                  '.OOO.',
                  '...O.',
                  '.....'],
                 ['.....',
                  '..O..',
                  '..O..',
                  '.OO..',
                  '.....']]

L_SHAPE_TEMPLATE = [['.....',
                  '...O.',
                  '.OOO.',
                  '.....',
                  '.....'],  # NOQA
                 ['.....',
                  '..O..',
                  '..O..',
                  '..OO.',
                  '.....'],
                 ['.....',
                  '.....',
                  '.OOO.',
                  '.O...',
                  '.....'],
                 ['.....',
                  '.OO..',
                  '..O..',
                  '..O..',
                  '.....']]

T_SHAPE_TEMPLATE = [['.....',
                  '..O..',
                  '.OOO.',
                  '.....',
                  '.....'],  # NOQA
                 ['.....',
                  '..O..',
                  '..OO.',
                  '..O..',
                  '.....'],
                 ['.....',
                  '.....',
                  '.OOO.',
                  '..O..',
                  '.....'],
                 ['.....',
                  '..O..',
                  '.OO..',
                  '..O..',
                  '.....']]

SHAPES = {'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE}


def main():
    """Function."""
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BIGFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    BIGFONT = pygame.font.Font('freesansbold.ttf', 100)
    pygame.display.set_caption('Tetris')

    showTextScreen('Tetris')
    while True:  # Main game loop
        if random.randint(0, 1) == 0:
            pygame.mixer.music.load('tetrisb.mid')
        else:
            pygame.mixer.music.load('tetrisc.mid')
        pygame.mixer.music.play(-1, 0.0)
        runGame()
        pygame.mixer.music.stop()
        showTextScreen('Game Over')


def runGame():
    """Function."""
    # Setup variables for the start of the game
    board = getBlankBoard()
    lastMoveDownTime = time.time()
    lastMoveSidewaysTime = time.time()
    lastFallTime = time.time()
    movingDown = False  # Note: There is no movingUp variables
    movingLeft = False
    movingRight = False
    score = 0
    level, fallFreq = calculateLevelAndFallFreq(score)

    fallingPiece = getNewPiece()
    nextPiece = getNewPiece()

    while True:
        if fallingPiece is None:
            # No falling piece in play, start a new piece at the top
            fallingPiece = nextPiece
            nextPiece = getNewPiece()
            lastFallTime = time.time()  # reset lastFallTime

            if not isValidPosition(board, fallingPiece):
                return  # Can't fit new piece on board, game Over

        checkForQuit()
        for event in pygame.event.get():  # Event handling loop
            if event.type == KEYUP:
                if(event.key == K_p):
                    # Pausing the game
                    DISPLAYSURF.fill(BGCOLOR)
                    pygame.mixer.music.stop()
                    showTextScreen('Paused')
                    pygame.mixer.music.play(-1, 0.0)
                    lastFallTime = time.time()
                    lastMoveDownTime = time.time()
                    lastMoveSidewaysTime = time.time()
                elif (event.key == K_LEFT or event.key == K_a):
                    movingLeft = False
                elif (event.key == K_RIGHT or event.key == K_d):
                    movingRight = False
                elif (event.key == K_DOWN or event.key == K_s):
                    movingDown = False

            elif event.type == KEYDOWN:
                # moving the block sideways
                if (event.key == K_LEFT or event.key == K_a) and isValidPosition(board, fallingPiece, adjX=-1):
                    fallingPiece['x'] -= 1
                    movingLeft = True
                    movingRight = False
                    lastMoveSidewaysTime = time.time()

                elif (event.key == K_RIGHT or event.key == K_d) and isValidPosition(board, fallingPiece, adjX=1):
                    fallingPiece['x'] += 1
                    movingRight = True
                    movingLeft = False
                    lastMoveSidewaysTime = time.time()

                    # Rotating block if there is room to rotate
                elif (event.key == K_UP or event.key == K_w):
                    fallingPiece['rotation'] = (fallingPiece['rotation']+1) % len(SHAPES[fallingPiece['shape']])
                    if not isValidPosition(board, fallingPiece):
                        fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(SHAPES[fallingPiece['shape']])

                elif (event.key == K_q):
                    fallingPiece['rotation'] = (fallingPiece['rotation']-1) % len(SHAPES[fallingPiece['shape']])
                    if not isValidPosition(board, fallingPiece):
                        fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(SHAPES[fallingPiece['shape']])

                # Making the block fall faster with the down key
            elif (event.key == K_DOWN or event.key == K_s):
                movingDown = True
                if isValidPosition(board, fallingPiece, adjY=1):
                    fallingPiece['y'] += 1
                lastMoveDownTime = time.time()

            elif event.key == K_SPACE:
                movingDown = False
                movingLeft = False
                movingRight = False
                for i in range(1, BOARDHEIGHT):
                    if not isValidPosition(board, fallingPiece, adjY=i):
                        break
                fallingPiece['y'] += i - 1

        # Handle moving the block because of user input
        if (movingLeft or movingRight) and time.time() - lastMoveSidewaysTime > MOVESIDEWAYSFREQ:
            if movingLeft and isValidPosition(board, fallingPiece, adjX=-1):
                fallingPiece['x'] -= 1
            elif movingRight and isValidPosition(board, fallingPiece, adjX=1):
                fallingPiece['x'] += 1
            lastMoveSidewaysTime = time.time()

        if movingDown and time.time() - lastMoveDownTime > MOVEDOWNFREQ and isValidPosition(board, fallingPiece, adjY=1):
            fallingPiece['y'] += 1
            lastMoveDownTime = time.time()

        # let the piece fall if its time to fall
        if time.time() - lastFallTime > fallFreq:
            # See if the piece has landed
            if not isValidPosition(board, fallingPiece, adjY=1):
                # falling piece has landed, set it on the board
                addToBoard(board, fallingPiece)
                score += removeCompleteLines(board)
                level, fallFreq = calculateLevelAndFallFreq(score)
                fallingPiece = None
            else:
                # Piece did not land, just move the block down
                fallingPiece['y'] += 1
                lastFallTime = time.time()

        # Drawing everything on the screen
        DISPLAYSURF.fill(BGCOLOR)
        drawBoard(board)
        drawStatus(score, level)
        drawNextPiece(nextPiece)
        if fallingPiece is not None:
            drawPiece(fallingPiece)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def makeTextObjs(text, font, color):
    """Function."""
    surf = font.render(text, True, color)
    return surf, surf.get_rect()


def terminate():
    """Function."""
    pygame.quit()
    sys.exit()


def checkForKeyPress():
    """Function."""
    # Go through event queue looking for KEYUP
    # Grab keydown events
    checkForQuit()

    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type is KEYDOWN:
            continue
        return event.key
    return None


def showTextScreen(text):
    """Function."""
    # Display large text until key is pressed
    # text shadow
    titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTSHADOWCOLOR)
    titleRect.center = (int(WINDOWWIDTH/2), int(WINDOWHEIGHT / 2))
    DISPLAYSURF.blit(titleSurf, titleRect)

    # Draw the text
    titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTCOLOR)
    titleRect.center = (int(WINDOWWIDTH/2)-3, int(WINDOWHEIGHT/2)-3)
    DISPLAYSURF.blit(titleSurf, titleRect)

    # Draw the additional "Press a key to play" text
    pressKeySurf, pressKeyRect = makeTextObjs('Press a key to play.', BASICFONT, TEXTCOLOR)
    pressKeyRect.center = (int(WINDOWWIDTH/2), int(WINDOWHEIGHT / 2) + 100)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

    while checkForKeyPress() is None:
        pygame.display.update()
        FPSCLOCK.tick()


def checkForQuit():
    """Function."""
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)


def calculateLevelAndFallFreq(score):
    """Function."""
    # Based on score return level and how many seconds pass until new piece falls one space

    level = int(score/10) + 1
    fallFreq = 0.27 - (level * 0.02)
    return level, fallFreq


def getNewPiece():
    """Function."""
    # return a random new piece in a random rotation and color
    shape = random.choice(list(SHAPES.keys()))
    newPiece = {'shape': shape,
        'rotation': random.randint(0, len(SHAPES[shape])-1),
        'x': int(BOARDWIDTH/2) - int(TEMPLATEWIDTH / 2),
        'y': -2,  # Start it above the board
        'color': random.randint(0, len(COLORS)-1)}  # NOQA
    return newPiece


def addToBoard(board, piece):
    """Function."""
    # fill in the board based on piece's location, shape and rotation
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            if SHAPES[piece['shape']][piece['rotation']][y][x] != BLANK:
                board[x + piece['x']][y + piece['y']] = piece['color']


def getBlankBoard():
    """Function."""
    # Create and return a new blank board data structure
    board = []
    for i in range(BOARDWIDTH):
        board.append([BLANK] * BOARDHEIGHT)
    return board


def isOnBoard(x, y):
    """Function."""
    return x >= 0 and x < BOARDWIDTH and y < BOARDHEIGHT


def isValidPosition(board, piece, adjX=0, adjY=0):
    """Function."""
    # Return True if the piece is within the board and not colliding
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            isAboveBoard = y + piece['y'] + adjY < 0
            if isAboveBoard or SHAPES[piece['shape']][piece['rotation']][y][x] == BLANK:
                continue
            if not isOnBoard(x + piece['x'] + adjX, y + piece['y'] + adjY):
                return False
            if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != BLANK:
                return False
    return True


def isCompleteLine(board, y):
    """Function."""
    # Return True if the line filled with boxes with no gaps
    for x in range(BOARDWIDTH):
        if board[x][y] == BLANK:
            return False
    return True


def removeCompleteLines(board):
    """Function."""
    # Remove completed lines on the board, move everything
    numLinesRemoved = 0
    y = BOARDHEIGHT - 1
    while y >= 0:
        if isCompleteLine(board, y):
            # Remove the line and pull boces down by one lines
            for pullDownY in range(y, 0, -1):
                for x in range(BOARDWIDTH):
                    board[x][pullDownY] = board[x][pullDownY-1]
            # Set very top line to blank
            for x in range(BOARDWIDTH):
                board[x][0] = BLANK
            numLinesRemoved += 1
            # Note on the next iteration of the loop, y is the S_SHAPE_TEMPLATE
            # So that if the line was pulled down is also completed, it will be removed
        else:
            y -= 1  # Move on to check next row up
    return numLinesRemoved


def convertToPixelCoords(boxx, boxy):
    """Convert to pixel coords."""
    return (XMARGIN + (boxx * BOXSIZE)), (TOPMARGIN + (boxy * BOXSIZE))


def drawBoard(board):
    """Convert to pixel coords."""
    pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (XMARGIN - 3, BOXSIZE * BOARDWIDTH, BOXSIZE * BOARDHEIGHT))
    # Draw individual boxes on the board
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            drawBox(x, y, board[x][y])


def drawStatus(score, level):
    """Convert to pixel coords."""
    scoreSurf = BASICFONT.render('SCORE: %s' % score, True, TEXTCOLOR)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 150, 20)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

    # Draw the level text
    levelSurf = BASICFONT.render('Level: %s' % level, True, TEXTCOLOR)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (WINDOWWIDTH - 150, 50)
    DISPLAYSURF.blit(levelSurf, levelRect)


def drawPiece(piece, pixelx=None, pixely=None):
    """Convert to pixel coords."""
    shapeToDraw = SHAPES[piece['shape']][piece['rotation']]
    if pixelx is None and pixely is None:
        # If pixelx and pixely hasnt been specified, use the location stored in the piece data structure
        pixelx, pixely = convertToPixelCoords(piece['x'], piece['y'])

    # Draw each of the blocks that make up the piece
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            if shapeToDraw[y][x] is not BLANK:
                drawBox(None, None, piece['color'], pixelx+(x * BOXSIZE), pixely+(y * BOXSIZE))


def drawNextPiece(piece):
    """Draw the next text."""
    nextSurf = BASICFONT.render('Next:', True, TEXTCOLOR)
    nextRect = nextSurf.get_rect()
    nextRect.topleft = (WINDOWWIDTH - 120, 80)
    DISPLAYSURF.blit(nextSurf, nextRect)
    # Draw the next piece
    drawPiece(piece, pixelx=WINDOWWIDTH-120, pixely=100)

if __name__ == '__main__':
    main()
