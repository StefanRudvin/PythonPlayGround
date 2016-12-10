#11. Feb 2015
#Stefan Rudvin from inventwithPython/pygame/ch3

import random, pygame, sys
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
REVEALSPEED = 8
BOXSIZE = 40
GAPSIZE = 10
BOARDWIDTH = 10
BOARDHEIGHT = 7
assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0,'Board needs to have even number of boxes for pairs of matches'
XMARGIN = int((WINDOWWIDTH-(BOARDWIDTH*(BOXSIZE + GAPSIZE)))/2)
YMARGIN = int((WINDOWHEIGHT-(BOARDHEIGHT*(BOXSIZE + GAPSIZE)))/2)

#Colours RGB
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH*BOARDHEIGHT,"Board is too big for the number of shapes/colors defined."

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

    mousex = 0 #store x coordinate of mouse
    mousey = 0 #store y coordinate
    pygame.display.set_caption('Memory Game')

    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)

    firstSelection = None #Stores x,y of clicked boxes

    DISPLAYSURF.fill(BGCOLOR)
    startGameAnimation(mainBoard)

    while True:
        mouseClicked = False

        DISPLAYSURF.fill(BGCOLOR) #draw window
        drawBoard(mainBoard,revealedBoxes)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex,mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        boxx, boxy = getBoxAtPixel(mousex, mousey)
        if boxx != None and boxy != None:
            #Mouse is currently over a boxx
            if not revealedBoxes[boxx][boxy]:
                drawHighlightBox(boxx,boxy)
            if not revealedBoxes[boxx][boxy] and mouseClicked:
                revealBoxesAnimation(mainBoard,[(boxx,boxy)])
                revealedBoxes[boxx][boxy] = True
                #Set box as revealed
                if firstSelection == None:
                    firstSelection = (boxx,boxy)
                    #The current box was the first box clicked
                else:
                    #the current box was the second box clicked
                    #CHeck if theres a match
                    icon1shape,icon1color = getShapeAndColor(mainBoard,firstSelection[0],firstSelection[1])
                    icon2shape, icon2color = getShapeAndColor(mainBoard,boxx,boxy)

                    if icon1shape != icon2shape or icon1color != icon2color:
                        #icons don't match. Re-cover up both selection
                        pygame.time.wait(10000) #= 1sec
                        coverBoxesAnimation(mainBoard,[(firstSelection[0],firstSelection[1]),(boxx,boxy)])
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxx][boxy] = False
                    elif hasWon(revealedBoxes):
                        gameWonAnimation(mainBoard)
                        pygame.time.wait(2000)

                        #Reset the Board
                        mainBoard = getRandomizedBoard()
                        revealedBoxes = generateRevealedBoxesData(False)

                        #Show the fully unrevealed board for a second
                        drawBoard(mainBoard,revealedBoxes)
                        pygame.display.update()
                        pygame.time.wait(1000)

                        #Replay the start game animation
                        startGameAnimation(mainBoard)

                    firstSelection = None #reset firstSelection variable

                #redraw the screen and wait a clock tick
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)
    return revealedBoxes

def getRandomizedBoard():
    #Get a list of every possible shape in every colors
    icons = []
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append((shape,color))

    random.shuffle(icons) #Randomize order of icons list
    numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2) #Calulate how many icons are needed
    icons = icons[:numIconsUsed] * 2 #Make two of each
    random.shuffle(icons)

    #Create board data structure with randomly placed icons
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(icons[0])
            del icons[0] #remove the icons as we assign them
        board.append(column)
    return board

def splitIntoGroupsOf(groupSize, theList):
    #Splits a list into a list of lists, where the inner lists have at
    #the most groupsize number of items
    result = []
    for i in range(0,len(theList),groupSize):
        result.append(theList[i:i + groupSize])
    return result

def leftTopCoordsOfBox(boxx, boxy):
    #Convert board coordinates to pixel coordinates
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return (left,top)

def getBoxAtPixel(x,y):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left,top = leftTopCoordsOfBox(boxx,boxy)
            boxRect = pygame.Rect(left,top,BOXSIZE,BOXSIZE)
            if boxRect.collidepoint(x,y):
                return (boxx,boxy)
    return (None,None)

def drawIcon(shape,color,boxx,boxy):
    quarter = int(BOXSIZE * 0.25)
    half = int(BOXSIZE * 0.5)

    left,top = leftTopCoordsOfBox(boxx,boxy) #get pixel coords from board
    if shape == DONUT:
        pygame.draw.circle(DISPLAYSURF,color,(left+half,top + half),half-5)
        pygame.draw.circle(DISPLAYSURF,BGCOLOR,(left + half,top+half),quarter -5)
    elif shape == SQUARE:
        pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top + quarter, BOXSIZE - half, BOXSIZE - half))
    elif shape == DIAMOND:
        pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top), (left + BOXSIZE - 1, top + half), (left + half, top + BOXSIZE - 1), (left, top + half)))
    elif shape == LINES:
        for i in range(0,BOXSIZE,4):
            pygame.draw.line(DISPLAYSURF, color, (left, top + i), (left + i, top))
            pygame.draw.line(DISPLAYSURF, color, (left + i, top + BOXSIZE - 1), (left + BOXSIZE - 1, top + i))
    elif shape == OVAL:
        pygame.draw.ellipse(DISPLAYSURF,color,(left,top + quarter,BOXSIZE,half))

def getShapeAndColor(board,boxx,boxy):
    #Shape value for x,y spot is stored in board[x][y][0]
    #Color is stored in board[x][y][1]
    return board[boxx][boxy][0],board[boxx][boxy][1]

def drawBoxCovers(board,boxes,coverage):
    #Shape value for x,y spot is stored in board[x][y][0]
    #Color is stored in board[x][y][1]
    for box in boxes:
        left, top = leftTopCoordsOfBox(box[0],box[1])
        pygame.draw.rect(DISPLAYSURF,BGCOLOR,(left,top,BOXSIZE,BOXSIZE))
        shape, color = getShapeAndColor(board, box[0], box[1])
        drawIcon(shape, color, box[0], box[1])
        if coverage > 0: #Only draw the cover if there is a coverage
            pygame.draw.rect(DISPLAYSURF,BOXCOLOR,(left,top,coverage,BOXSIZE))
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def revealBoxesAnimation(board,boxesToReveal):
    #Do the animation
    for coverage in range(BOXSIZE,(-REVEALSPEED) -1, -REVEALSPEED):
        drawBoxCovers(board,boxesToReveal,coverage)

def coverBoxesAnimation(board,boxesToCover):
    #Do the box cover animation
    for coverage in range(0,BOXSIZE + REVEALSPEED,REVEALSPEED):
        drawBoxCovers(board,boxesToCover,coverage)

def drawBoard(board,revealed):
    #Draw all the boces in their covered or revealed state.
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left,top = leftTopCoordsOfBox(boxx,boxy)
            if not revealed[boxx][boxy]:
                #Draw covered box
                pygame.draw.rect(DISPLAYSURF,BOXCOLOR,(left,top,BOXSIZE,BOXSIZE))
            else:
                #Draw revealed icons
                shape,color = getShapeAndColor(board,boxx,boxy)
                drawIcon(shape,color,boxx,boxy)

def drawHighlightBox(boxx,boxy):
    left,top = leftTopCoordsOfBox(boxx,boxy)
    pygame.draw.rect(DISPLAYSURF,HIGHLIGHTCOLOR,(left - 5,top - 5,BOXSIZE + 10, BOXSIZE + 10),4)

def startGameAnimation(board):
    #Randomly reveal the boxes 8 at a time
    coveredBoxes = generateRevealedBoxesData(False)
    boxes = []
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            boxes.append((x,y))
    random.shuffle(boxes)
    boxGroups = splitIntoGroupsOf(8,boxes)

    drawBoard(board,coveredBoxes)
    for boxGroup in boxGroups:
        revealBoxesAnimation(board,boxGroup)
        coverBoxesAnimation(board,boxGroup)

def gameWonAnimation(board):
    #Flash the background color
    coveredBoxes = generateRevealedBoxesData(True)
    color1= LIGHTBGCOLOR
    color2= BGCOLOR

    for i in range(13):
        color1,color2 = color2,color1 #swap colors
        DISPLAYSURF.fill(color1)
        drawBoard(board,coveredBoxes)
        pygame.display.update()
        pygame.time.wait(300)

def hasWon(revealedBoxes):
    #Return true if all boxes have been revealed
    for i in revealedBoxes:
        if False in i:
            return False #Return false if boxes are covered
    return True

if __name__=='__main__':
    main()
