import pygame, random, sys
import shelve
from pygame.locals import *
import sys

#variables
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BLUE      = (  0,  51, 102)
BGCOLOR   = BLACK

UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

FPS = 30
WINDOWWIDTH = 1200
WINDOWHEIGHT = 800
CELLSIZE = 20

# Make list of empty lists

def main(FPS):
    global DISPLAY, lives, FPSCLOCK, BASICFONT

    #Setup pyGame
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption('Pathfinding')
    lives = 3
    BASICFONT = pygame.font.Font('freesansbold.ttf',18)

    showStartScreen()
    #Make Game() loop
    while True:

        if not runGame(FPS,lives):
            lives -= 1
            print(lives)
        if lives == 0:
            showGameOverScreen()

def runGame(FPS,lives):

    #Setup game variables
    playerStartX = 20
    playerStartY = 10

    aiStartX = 10
    aiStartY = 10

    #Game object is a dictionary of player and ai positions
    #gameObject['player'] = position
    gameObject = gameInit(playerStartX,playerStartY,aiStartX,aiStartY)
    playerPos = (gameObject['playerx'],gameObject['playery'])
    aiPos = (gameObject['aix'],gameObject['aiy'])

    #Game Variables
    aiTrail = []
    aiMoves = 0
    wall = []
    wall.append((15,10)) ; wall.append((6,6)) ; wall.append((1,1)) ; wall.append((5,5))

    #Main game loop
    while True:
        PDIRECTION = 0
        movePlayer = False
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                movePlayer = True
                if (event.key == K_LEFT or event.key == K_a) and PDIRECTION != RIGHT:
                    PDIRECTION = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and PDIRECTION != LEFT:
                    PDIRECTION = RIGHT
                elif (event.key == K_UP or event.key == K_w) and PDIRECTION != DOWN:
                    PDIRECTION = UP
                elif (event.key == K_DOWN or event.key == K_s) and PDIRECTION != UP:
                    PDIRECTION = DOWN
                elif event.key == K_ESCAPE:
                    terminate()
                #print(PDIRECTION)
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                mousex = int(mouse[0]/20)
                mousey = int(mouse[1]/20)

                wallRemove = 0

                if isBlocked(mousex,mousey,wall):
                    wall.remove((mousex,mousey))
                else:
                    wall.append((mousex,mousey))

        DISPLAY.fill(BLACK)

        ###### AI SECTION START ##########

        #Returns "DOWN", "UP", etc
        AIDIRECTION = heuristics(*playerPos,*aiPos)

        if Lost(*playerPos,*aiPos):
            return False

        aiNextPos = moveAi(*aiPos,AIDIRECTION)

        if not isBlocked(*aiNextPos,wall):
            aiTrail.append(aiPos) # Add previous position to trail
            aiPos = aiNextPos
            aiMoves += 1
        else:
            pass

        ###### AI SECTION END ##########

        playerNextPos = moveAi(*playerPos,PDIRECTION)

        if movePlayer:
            if not isBlocked(*playerNextPos,wall):
                playerPos = playerNextPos
                movePlayer = False
            else:
                pass

        #Draw aiTrail
        for i, (x,y) in enumerate(aiTrail):
            drawRect(*convertToPixel(*aiTrail[i]), DARKGRAY)

        #Draw AI
        drawRect(*convertToPixel(*aiPos), GREEN)

        #Draw player
        drawRect(*convertToPixel(*playerPos),RED)

        #Draw wall
        for i, (x,y) in enumerate(wall):
            drawRect(*convertToPixel(*wall[i]), WHITE)

        drawGrid()

        #Draw aiMoves
        message_display_lr('aiMoves: ' + str(aiMoves))

        message_display_ll('Lives left: ' + str(lives))

        #if aiPos == playerPos:
        #    lives -= 1
        #    print(lives)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def Lost(playerx,playery,aix,aiy):
    xdistance = abs(playerx-aix)
    ydistance = abs(playery-aiy)
    if xdistance == 0:
        if ydistance == 0:
            return True

def showStartScreen():

    while True:
        DISPLAY.fill(BGCOLOR)
        number = 5

        rectangle = Rect(0, 0, 400, 200)
        rectangle.center = (WINDOWWIDTH/2,WINDOWHEIGHT/2)
        pygame.draw.rect(DISPLAY, DARKGREEN, rectangle)

        message_display("PATHFIND")

        drawPressKeyMsg()

        if checkforKeyPress():
            pygame.event.get() #clear event queue
            return

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def showGameOverScreen():
    while True:
        DISPLAY.fill(BLACK)
        message_display("GAME OVER")
        drawPressKeyMsg()
        if checkforKeyPress():
            pygame.event.get() #clear event queue
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press a key to play.',True,WHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAY.blit(pressKeySurf,pressKeyRect)

def checkforKeyPress():
    if len(pygame.event.get(QUIT))>0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

def drawRect(x,y,colour):
    pygame.draw.rect(DISPLAY, colour, (x,y,20,20), 0) #Inner
    pygame.draw.rect(DISPLAY, WHITE, (x,y,20,20), 2) #Outer

def drawGrid():
    for x in range(0, WINDOWWIDTH,CELLSIZE): #Draw vertical lines
        pygame.draw.line(DISPLAY,DARKGRAY,(x,0),(x,WINDOWHEIGHT))

    for y in range(0,WINDOWHEIGHT,CELLSIZE): #Draw horizontal lines
        pygame.draw.line(DISPLAY,DARKGRAY,(0,y),(WINDOWWIDTH,y))

def heuristics(playerx,playery,aix,aiy):
    xdistance = abs(playerx-aix)
    ydistance = abs(playery-aiy)

    if xdistance < ydistance: #Ai is further in Y direction
        if playery > aiy:
            return "DOWN"
        else:
            return "UP"
    elif xdistance > ydistance:
        if playerx > aix: #Ai is futher in X direction
            return "RIGHT"
        else:
            return "LEFT"
    elif xdistance == ydistance: #Same distance
        if playerx > aix: # Player is 'EAST'
            if aiy > playery: # Player is northeast
                randomNumber = random.randint(0, 1)
                if randomNumber == 0:
                    return "RIGHT"
                else:
                    return "UP"
            else: #Player is southeast
                randomNumber = random.randint(0, 1)
                if randomNumber == 0:
                    return "RIGHT"
                else:
                    return "DOWN"
        else: #Player is 'WEST'
            if aiy > playery: # Player is northwest
                randomNumber = random.randint(0, 1)
                if randomNumber == 0:
                    return "LEFT"
                else:
                    return "UP"
            else: #Player is southwest
                randomNumber = random.randint(0, 1)
                if randomNumber == 0:
                    return "LEFT"
                else:
                    return "DOWN"

def moveAi(aix, aiy, direction):
    if direction == "UP":
        return aix, aiy - 1
    elif direction == "DOWN":
        return aix, aiy + 1
    elif direction == "LEFT":
        return aix - 1, aiy
    elif direction == "RIGHT":
        return aix + 1, aiy

def isBlocked(aix,aiy, wall):
    for i, (x,y) in enumerate(wall):
        if x == aix and y == aiy:
            return True
    #Add sides of the game
    #print(int(WINDOWHEIGHT/20),aiy)
    if aix > (int(WINDOWWIDTH/20))-1:
        return True
    if aiy < 0:
        return True
    return False

def gameInit(playerx,playery,aix,aiy):
    gameObject={}
    gameObject['playerx'] = playerx
    gameObject['playery'] = playery
    gameObject['aix'] = aix
    gameObject['aiy'] = aiy

    return gameObject

def convertToPixel(x,y):
    return int(x*20), int(y*20)

def terminate():
    pygame.quit()
    sys.exit()

def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def message_display_lr(text):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((WINDOWWIDTH-70),(WINDOWHEIGHT-20))
    DISPLAY.blit(TextSurf, TextRect)

def message_display_ll(text):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((70),(WINDOWHEIGHT-20))
    DISPLAY.blit(TextSurf, TextRect)

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((WINDOWWIDTH/2),(WINDOWHEIGHT/2))
    DISPLAY.blit(TextSurf, TextRect)

# END OF FILE
if __name__ == '__main__':
    main(FPS)
