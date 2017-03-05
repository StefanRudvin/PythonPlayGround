import pygame, random, sys
from pygame.locals import *

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return

def playerHasHitGhost(playerRect, ghosts):
    for g in ghosts:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def drawText(text,font,surface,x,y):
    textobj = font.render(text,1,TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj,textrect)

def validMove(playerRect, )

#Constants
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
TEXTCOLOR = (255,255,255)
BACKGROUNDCOLOR = (0,0,0)
FPS = 40
MOVESPEED = 4

#Initialize Pygame
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption('Pacman')
pygame.mouse.set_visible(False)

font = pygame.font.SysFont(None,48)

#Setup music & mixer
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('maio.mid')

#Setup player and ghost images
playerImage = pygame.image.load('Pacman.png')
playerRect = playerImage.get_rect()
ghostred = pygame.image.load('redghost.png')
ghostblue = pygame.image.load('blueghost.png')
ghostpink = pygame.image.load('pinkghost.png')
ghostyellow = pygame.image.load('yellowghost.png')

#Show the start screen
drawText('PACMAN',font,windowSurface,(WINDOWWIDTH/3),(WINDOWHEIGHT/3))
drawText('Press a key to start',font,windowSurface,(WINDOWWIDTH/3)-30,(WINDOWHEIGHT/3)+50)
pygame.display.update()
waitForPlayerToPressKey()
