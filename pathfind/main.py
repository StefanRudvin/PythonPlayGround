import pygame, random, sys
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

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def main(FPS):
    global DISPLAY, lives, FPSCLOCK, BASICFONT

    #Setup pyGame
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption('Pathfinder')
    lives = 3
    BASICFONT = pygame.font.Font('freesansbold.ttf',18)

    startMode = "Basic"

    modes = ("Basic","Random","B-First")
    #mode = showStartScreen()
    mode = showStartScreen(*modes,startMode)
    #Make Game() loop

    while True:
        if not runGame(FPS,lives,mode,modes):
            lives -= 1
            print("Lives left: " + str(lives))
        if lives == 0:
            showGameOverScreen()
            lives = 3

def runGame(FPS,lives,mode,modes):

    #Setup game variables
    playerStartX = 50
    playerStartY = 20

    aiStartX = 10
    aiStartY = 20

    #Game object is a dictionary of player and ai positions
    #gameObject['player'] = position
    gameObject = gameInit(playerStartX,playerStartY,aiStartX,aiStartY)
    playerPos = (gameObject['playerx'],gameObject['playery'])
    aiPos = (gameObject['aix'],gameObject['aiy'])

    #Game Variables
    aiTrail = []
    aiMoves = 0
    wall = []
    wall.append((30,20)) ; wall.append((30,21)) ; wall.append((30,22)); wall.append((30,19)); wall.append((30,18))
    freeze = False
    placePlayer = False
    placeAi = False
    futureNode = ""


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
                elif event.key == K_m:
                    if mode == modes[0]:
                        mode = modes[1]
                    elif mode == modes[1]:
                        mode = modes[2]
                    elif mode == modes[2]:
                        mode = modes[0]
                elif event.key == K_f:
                    if freeze == True:
                        freeze = False
                    else:
                        freeze = True
                elif event.key == K_p:
                    if placePlayer == True:
                        placePlayer = False
                    else:
                        placePlayer = True
                        placeAi = False
                elif event.key == K_o:
                    if placeAi == True:
                        placeAi = False
                    else:
                        placeAi = True
                        placePlayer = False
                elif event.key == K_ESCAPE:
                    terminate()
                #print(PDIRECTION)
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                mousex = int(mouse[0]/20)
                mousey = int(mouse[1]/20)

                if placePlayer:
                    playerPos = (mousex,mousey)
                elif placeAi:
                    aiPos = (mousex,mousey)
                else:
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

        #If it has been blocked before, run this!
        if aiNextPos == futureNode:
            if mode == "Random":
                AIDIRECTION = randomDirection()
                print("Random func return: " + str(AIDIRECTION))

            aiNextPos = moveAi(*aiPos,AIDIRECTION)

        futureNode = aiNextPos

        if not freeze:
            if not isBlocked(*aiNextPos,wall):
                aiTrail.append(aiPos) # Add previous position to trail
                aiPos = aiNextPos
                aiMoves += 1
            else:
                pass

        ###### AI SECTION END ##########

        playerNextPos = moveAi(*playerPos,PDIRECTION)

        if movePlayer and not PDIRECTION == 0:
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
        #Draw aiMoves and life
        message_display_lr('aiMoves: ' + str(aiMoves))
        message_display_ll('Lives left: ' + str(lives))

        #Modified variables
        if freeze == True:
            message_display_ll('Freeze On', 120)
        else:
            message_display_ll('Freeze Off', 120)

        if placePlayer == True:
            message_display_ll('Pmove On', 240)
        else:
            message_display_ll('Pmove Off', 240)

        if placeAi == True:
            message_display_ll('Aimove On', 360)
        else:
            message_display_ll('Aimove Off', 360)

        message_display_ll(mode, 480)


        pygame.display.update()
        FPSCLOCK.tick(FPS)

def showStartScreen(mode1,mode2,mode3,mode):

    while True:
        DISPLAY.fill(BGCOLOR)

        if mode == mode1:
            colour = GREEN
        if mode == mode2:
            colour = RED
        if mode == mode3:
            colour = DARKGRAY

        rectangle = Rect(0, 0, 400, 200)
        rectangle.center = (WINDOWWIDTH/2,WINDOWHEIGHT/2)
        pygame.draw.rect(DISPLAY, colour, rectangle)

        message_display("PATHFINDER")

        WW = WINDOWWIDTH / 2
        WH = WINDOWHEIGHT / 2 + 180

        rectangleTuples = [(WW-220,WH,mode1),(WW,WH,mode2),(WW+220,WH,mode3)]

        for i, (a, b, c) in enumerate(rectangleTuples):
            rectangle = Rect(0, 0, 200, 100)
            rectangle.center = (a,b)
            pygame.draw.rect(DISPLAY, colour, rectangle)

            message_display_custom(c,a,b)

        drawPressKeyMsg()

        #Select mode
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                mousex = int(mouse[0])
                mousey = int(mouse[1])
                WWH = WH-50
                if mousey > WWH and mousey < WH+100:
                    if mousex > WW-100 and mousex < WW+100:
                        mode = mode2
                    if mousex > WW-220 and mousex < WW-120:
                        mode = mode1
                    if mousex > WW+120 and mousex < WW+220:
                        mode = mode3
            if event.type == pygame.KEYUP:
                return mode

        message_display_ll('Mode selected: ' + str(mode),60)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def Lost(playerx,playery,aix,aiy):
    xdistance = abs(playerx-aix)
    ydistance = abs(playery-aiy)
    if xdistance == 0:
        if ydistance == 0:
            return True

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

    pressKeySurf = BASICFONT.render('Press F to Freeze.',True,WHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 250, 20)
    DISPLAY.blit(pressKeySurf,pressKeyRect)

    pressKeySurf = BASICFONT.render('Press P to Move Player.',True,WHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 250, 40)
    DISPLAY.blit(pressKeySurf,pressKeyRect)

    pressKeySurf = BASICFONT.render('Press O to Move Ai.',True,WHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 250, 60)
    DISPLAY.blit(pressKeySurf,pressKeyRect)

    pressKeySurf = BASICFONT.render('WASD to move player.',True,WHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 250, 80)
    DISPLAY.blit(pressKeySurf,pressKeyRect)

    pressKeySurf = BASICFONT.render('Click to add walls.',True,WHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 250, 100)
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

def message_display_lr(text,offset = 0):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((WINDOWWIDTH-70 - offset),(WINDOWHEIGHT-20))
    DISPLAY.blit(TextSurf, TextRect)

def message_display_ll(text,offset = 0):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((70 + offset),(WINDOWHEIGHT-20))
    DISPLAY.blit(TextSurf, TextRect)

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((WINDOWWIDTH/2),(WINDOWHEIGHT/2))
    DISPLAY.blit(TextSurf, TextRect)

def message_display_custom(text,width,height):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width),(height))
    DISPLAY.blit(TextSurf, TextRect)

def randomDirection():
    randomNumber = random.randint(0, 3)
    if randomNumber == 0:
        return "RIGHT"
    elif randomNumber == 1:
        return "LEFT"
    elif randomNumber == 2:
        return "DOWN"
    elif randomNumber == 3:
        return "UP"

#BREADTHFIRST = breadthfirst(*playerPos,*aiPos,wall)

def breadthfirst(playerx,playery,aix,aiy,wall):
    frontier = queue()
    frontier.put((aix,aiy))
    visited = {}

    while not frontier.empty():
        current = frontier.get()
        for next in graph.neighbors(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True

def neighbors(node):
    dirs = [[1,0],[0,1],[-1,0],[0,-1]]
    for dir in dirs:
        return [node[0] + dir[0], node[1] + dir[1]]


def isNeighbour(node, mapObj):
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for dir in dirs:
        neighbor = [node[0] + dir[0], node[1] + dir[1]]
        if not isWall(mapObj,neighbor[0],neighbor[1]):
            result.append(neighbor)
    return result

# END OF FILE
if __name__ == '__main__':
    main(FPS)
