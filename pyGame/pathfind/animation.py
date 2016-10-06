import pygame
from pygame.locals import *
import sys

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

def main():
    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((640,480))

    circleStart = 0
    houseStart = 600


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit(); exit()

        screen.fill(black)

        pygame.draw.circle(screen, blue, (circleStart,200), 50, 5)

        drawHouse(houseStart,300,150,150,screen, blue)

        pygame.display.update()

        circleStart += 1
        houseStart -= 1

        ### Making motion slower
        #pygame.time.delay(5)

        #Better way is to use a clock
        #msElapsed = clock.tick(60)


def drawHouse(x, y, width, height, screen, color):
    points = [(x,y- ((2/3.0) * height)), (x,y), (x+width,y), (x+width,y-(2/3.0) * height),
        (x,y- ((2/3.0) * height)), (x + width/2.0,y-height), (x+width,y-(2/3.0)*height)]
    lineThickness = 2
    pygame.draw.lines(screen, color, False, points, lineThickness)

if __name__ == '__main__':
    main()
