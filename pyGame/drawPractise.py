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

    screen = pygame.display.set_mode((640,480))

    screen.fill(red)

    pygame.draw.lines(screen, black, False, [(100,100), (150,200), (200,100)], 2)

    pygame.draw.rect(screen, pink, (400,400,100,20), 3)

    pygame.draw.circle(screen, blue, (400,200), 50, 5)

    pygame.draw.arc(screen, green, (10,10,50,50), 0, 1.57, 2)

    drawHouse1(300, 300, 150, 150, screen, white)

    drawHouse2(460,300,150,150,screen, blue)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit(); exit()
            elif event.key == K_ESCAPE:
                pygame.quit(); exit()
        pass

# First way of drawing house
def drawHouse1(x, y, width, height, screen, color):
    points = [(x,y- ((2/3.0) * height)), (x,y), (x+width,y), (x+width,y-(2/3.0) * height),
        (x,y- ((2/3.0) * height)), (x + width/2.0,y-height), (x+width,y-(2/3.0)*height)]
    lineThickness = 2
    pygame.draw.lines(screen, color, False, points, lineThickness)

#Use one function for house frame, another for drawing lines

def makeHouseFrame(x,y,width,height):
   points = [] # start with an empty list
   points.append((x,y- ((2/3.0) * height))) # top of 1st story, upper left
   points.append((x,y))  # lower left corner
   points.append((x+width,y)) # lower right corner
   points.append((x+width,y-(2/3.0) * height)) # top of 1st story upper right
   points.append((x,y- ((2/3.0) * height))) # top of first story, upper left
   points.append((x + width/2.0,y-height)) # top of roof
   points.append((x+width,y-(2/3.0)*height)) # top of 1st story, upper right
   return points

def drawHouse2(x,y,width,height,screen,color):
   lineThickness = 2
   pygame.draw.lines(screen, color, False,
           makeHouseFrame(x,y,height,width), lineThickness)

if __name__ == '__main__':
    main()
