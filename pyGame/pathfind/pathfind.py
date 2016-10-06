import random, sys, os, pygame, ghostai, readfile, func, os.path
from pygame.locals import *
from func import *
from ghostai import *
from readfile import *

#Pygame variables
FPS = 30
WINWIDTH = 1000
WINHEIGHT = 800
CELLSIZE = 20

HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

CELLWIDTH = int(WINWIDTH/CELLSIZE)
CELLHEIGHT = int(WINHEIGHT/CELLSIZE)

assert WINWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."

initialize()

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

WHITE     = (255, 255, 255)
BLACK = (0,0,0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BLUE = (0,51,102)
BGCOLOR = BLACK

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    #ghost = pygame.image.load('ghost.png')
    #print(ghostai.myvariable)
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH,WINHEIGHT))
    pygame.display.set_caption('Pathfinder')
    BASICFONT = pygame.font.Font('freesansbold.ttf',18)

    pygame.draw.line(DISPLAYSURF,BLACK,(20,0),(20,WINHEIGHT))

    pygame.display.update()

    print("Width cell size: ", WINWIDTH/CELLSIZE)
    print("Height cell size: ", WINHEIGHT/CELLSIZE)

    #while True:
    #    drawGrid()

    #showStartScreen(DISPLAYSURF,BASICFONT,FPSCLOCK,BGCOLOR)

    while True:
        runGame(FPS)
        #showGameOverScreen()

#Main game loop
def runGame(FPS):
    #Set start points for player and AI
    startx = random.randint(5, CELLWIDTH - 6)

    while True:
        drawGrid()

def drawGrid():
    for x in range(0, WINWIDTH,CELLSIZE): #Draw vertical lines
        pygame.draw.line(DISPLAYSURF,BLACK,(x,0),(x,WINHEIGHT))

    for y in range(0,WINHEIGHT,CELLSIZE): #Draw horizontal lines
        pygame.draw.line(DISPLAYSURF,WHITE,(0,y),(WINWIDTH,y))


if __name__ == '__main__':
    main()
