import pygame,sys,random
from pygame.locals import *

def doRectsOverlap(rect1,rect2):
    for a,b in [(rect1, rect2),(rect2,rect1)]:
        #Check if a's corners are inside b
        if ((isPointInsideRect(a.left,a.top,b)) or (isPointInsideRect(a.left,a.bottom,b)) or (isPointInsideRect(a.right,a.top,b)) or (isPointInsideRect(a.right,a.bottom,b))):
            return True

    return False

def isPointInsideRect(x,y,rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y<rect.bottom):
        return True
    else:
        return False

#setup pygame
pygame.init()
mainClock = pygame.time.Clock()

#Setup the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Collision Detection')

#Setup up direction
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9

MOVESPEED = 4

#Setup up the colours
BLACK = (0,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)

#Setup the bouncer and food data structures
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
bouncer = {'rect':pygame.Rect(300,100,50,50),'dir':UPLEFT}
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

#Run the game loop
while True:
    #Check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        #Add new food
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

     #Draw black background
    windowSurface.fill(BLACK)

     #Move the bouncer data structure
    if bouncer['dir'] == DOWNLEFT:
        bouncer['rect'].left -= MOVESPEED
        bouncer['rect'].top  += MOVESPEED
    if bouncer['dir'] == DOWNRIGHT:
        bouncer['rect'].left += MOVESPEED
        bouncer['rect'].top  += MOVESPEED
    if bouncer['dir'] == UPLEFT:
        bouncer['rect'].left -= MOVESPEED
        bouncer['rect'].top -= MOVESPEED
    if bouncer['dir'] == UPRIGHT:
        bouncer['rect'].left += MOVESPEED
        bouncer['rect'].top -= MOVESPEED

    #Check if the bouncer has moved out of the window
    if bouncer['rect'].top < 0:
        #Bouncer has moved past the top
        if bouncer['dir'] == UPLEFT:
            bouncer['dir'] = DOWNLEFT
        if bouncer['dir'] == UPRIGHT:
            bouncer['dir'] = DOWNRIGHT
    if bouncer['rect'].bottom > WINDOWHEIGHT:
        #past bottom
        if bouncer['dir'] == DOWNLEFT:
            bouncer['dir'] = UPLEFT
        if bouncer['dir'] == DOWNRIGHT:
            bouncer['dir'] = UPRIGHT
    if bouncer['rect'].left < 0:
        #Bouncer has moved past the left side
        if bouncer['dir'] == DOWNLEFT:
            bouncer['dir'] = DOWNRIGHT
        if bouncer['dir'] == UPLEFT:
            bouncer['dir'] = UPRIGHT
    if bouncer['rect'].right > WINDOWWIDTH:
        #Bouncer has moved past the right side
        if bouncer['dir'] == DOWNRIGHT:
            bouncer['dir'] = DOWNLEFT
        if bouncer['dir'] == UPRIGHT:
            bouncer['dir'] = UPLEFT

    #Draw the bouncer on the surface
    pygame.draw.rect(windowSurface, WHITE, bouncer['rect'])

    #Check if the bouncer has intersected with any food squares
    for food in foods[:]:
        if doRectsOverlap(bouncer['rect'],food):
            foods.remove(food)

    #Draw the food
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface,GREEN,foods[i])

    #Draw the window to the screen
    pygame.display.update()
    mainClock.tick(40)
