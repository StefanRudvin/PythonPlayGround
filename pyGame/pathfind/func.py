import random, sys, os, pygame, ghostai, readfile, pathfind
from pathfind import *

def initialize():
    ghostai.initialize()
    readfile.initialize()

def terminate():
    pygame.quit()
    sys.exit()

def showStartScreen(DISPLAYSURF,BASICFONT,FPSCLOCK,BGCOLOR):
    titleFont = pygame.font.Font('freesansbold.ttf',100)
    titleSurf = titleFont.render('Pathfinder',True,WHITE,DARKGREEN)

    while True:
        DISPLAYSURF.fill(BGCOLOR)
        titleRect = titleSurf.get_rect()
        titleRect.center = (WINWIDTH/2,WINHEIGHT/2)
        DISPLAYSURF.blit(titleSurf,titleRect)

        #Make function for keypress HERE

        pygame.display.update()
        FPSCLOCK.tick(FPS)
