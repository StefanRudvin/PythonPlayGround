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

#Total width and height of each tile in pixels
TILEWIDTH = 50
TILEHEIGHT = 50

HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

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
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    #pygame.image.load("/Dropbox/Code/Python/pyGame/pathfind/assets/ghost.png")
    #ghost = pygame.image.load('ghost.png')
    #print(ghostai.myvariable)
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH,WINHEIGHT))
    pygame.display.set_caption('Pathfinder')
    BASICFONT = pygame.font.Font('freesansbold.ttf',18)

    showStartScreen(DISPLAYSURF,BASICFONT,FPSCLOCK,BGCOLOR)

if __name__ == '__main__':
    main()
