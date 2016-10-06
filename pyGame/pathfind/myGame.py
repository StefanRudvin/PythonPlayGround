import pygame
from pygame.locals import *
import sys

WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BLUE      = (  0,  51, 102)
BGCOLOR   = BLACK

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20

# Make list of empty lists

def main():
    global DISPLAY

    #Setup pyGame
    pygame.init()
    clock = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

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

    wall = []
    wall.append((15,10))
    wall.append((6,6))

    #Animation Loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit(); exit()

        DISPLAY.fill(BLACK)

        ###### AI SECTION START ##########

        #Returns "DOWN", "UP", etc
        DIRECTION = heuristics(*playerPos,*aiPos)

        aiNextPos = moveAi(*aiPos,DIRECTION)

        if not isBlocked(*aiNextPos,wall):
            aiPos = aiNextPos
        else:
            pass

        ###### AI SECTION END ##########

        #Draw player
        drawRect(*convertToPixel(*playerPos),RED)

        #Draw AI
        drawRect(*convertToPixel(*aiPos), GREEN)

        #Draw wall
        for i, (x,y) in enumerate(wall):
            drawRect(*convertToPixel(*wall[i]), WHITE)

        drawGrid()

        pygame.display.update()

        #Better way is to use a clock
        msElapsed = clock.tick(60)

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
    else:
        raise Exception("Player lost!")

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
        else:
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

# END OF FILE
if __name__ == '__main__':
    main()
