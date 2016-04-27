import pygame,sys,time
from pygame.locals import *

#Setup pygame
pygame.init()

#Setup the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Animation')

#setup direction variables
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9

MOVESPEED = 4

#Setup the colours
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#Setup the block data structure
b1 = {'rect':pygame.Rect(300,80,50,100),'color':RED,'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(200,200,20,20),'color':GREEN,'dir':UPLEFT}
b3 = {'rect':pygame.Rect(100,150,60,60),'color':BLUE,'dir':DOWNLEFT}
b4 = {'rect':pygame.Rect(50,50,60,60),'color':GREEN,'dir':DOWNLEFT}
b5 = {'rect':pygame.Rect(20,20,20,20),'color':WHITE,'dir':DOWNLEFT}

blocks = [b1,b2,b3,b4,b5]

#Run the game loop
while True:
    #Check for quit event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Draw the black background
    windowSurface.fill(BLACK)

    for b in blocks:
        #move the block data structure
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top  += MOVESPEED
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top  += MOVESPEED
        if b['dir'] == UPLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top  -= MOVESPEED
        if b['dir'] == UPRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top  -= MOVESPEED

        #Check if the block has moved out of the window
        if b['rect'].top < 0:
            #Block has moved past the top
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
        if b['rect'].bottom > WINDOWHEIGHT:
            #Block has moved past the bottom
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
        if b['rect'].left < 0:
            #Block has moved past the left side
            if b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
        if b['rect'].right > WINDOWWIDTH:
            #Block has moved past the right side
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT
        #Draw the block onto the surface
        pygame.draw.rect(windowSurface,b['color'],b['rect'])

    #Draw the window to the screen
    pygame.display.update()
    time.sleep(0.02)
