import pygame, sys
from pygame.locals import *

#Setup pygame
pygame.init()

#Setup window
windowSurface = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption('Hello world!')

#setup the colours
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#Setup fonts
basicFont = pygame.font.SysFont(None,48)

#Setuptext
text = basicFont.render('Hello world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

#Draw the white background onto the surface
pygame.draw.polygon(windowSurface,GREEN,((146,0),(291,106),(236,277),(57,277),(0,106)))

#Draw a green polygon
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

#Draw blue lines on the surface
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)

#Draw blue circle on the surface
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

#Draw red ellipse
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

#Draw text rectancle background
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

#Get a pixel array of the surface
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLACK
del pixArray

#Draw text onto the surface
windowSurface.blit(text,textRect)

#Draw the window onto the screen
pygame.display.update()

#Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
