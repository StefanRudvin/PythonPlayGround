# Wormy: A copy of Nokia's worm game
# Code used from: http://inventwithpython.com/pygame/chapter6.html

import random, pygame, sys
import shelve
from pygame.locals import *

FPS = 25
WINDOWWIDTH = 860
WINDOWHEIGHT = 480
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH/CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT/CELLSIZE)

WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BLUE = (0,51,102)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0 #INdex of worm's HEAD

def main(FPS):
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf',18)
    pygame.display.set_caption('Worm')

    showStartScreen()
    while True:
        runGame(FPS)
        showGameOverScreen()

def runGame(FPS):
    #Set random start point
    startx = random.randint(5,CELLWIDTH - 6)
    starty = random.randint(5, CELLHEIGHT -6)
    wormCoords = [{'x':startx, 'y':starty},
    {'x':startx -1, 'y':starty},
    {'x':startx -2, 'y':starty}]
    direction = RIGHT

    #Star the apple in a random place.
    apple = getRandomLocation()
    wallapple = getRandomLocation() # go through walls apple
    apple3 = getRandomLocation()
    greyapple = getRandomLocation() # Reverses direction
    fastapple = getRandomLocation() # Makes FPS lower (Speed)

    reverse = 0 #Parameter for reverse
    loop = 100 #Loop timer for reverse

    wall = 0 #Parameter for going through walls
    wallloop = 200 #Loop timer for going through walls

    fast = 0 #Parameter for going lower
    fastloop = 50 #Loop timer for going slow

    while True: #Main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if reverse == 0:
                    if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                        direction = LEFT
                    elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                        direction = RIGHT
                    elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                        direction = UP
                    elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                        direction = DOWN
                    elif event.key == K_ESCAPE:
                        terminate()
                else:
                    if (event.key == K_LEFT or event.key == K_a) and direction != LEFT:
                        direction = RIGHT
                    elif (event.key == K_RIGHT or event.key == K_d) and direction != RIGHT:
                        direction = LEFT
                    elif (event.key == K_UP or event.key == K_w) and direction != UP:
                        direction = DOWN
                    elif (event.key == K_DOWN or event.key == K_s) and direction != DOWN:
                        direction = UP
                    elif event.key == K_ESCAPE:
                        terminate()
        if reverse == 1:
            loop -= 1
            if loop == 0:
                reverse = 0
                loop = 100
                print('Reverse over')

        if wall == 1:
            wallloop -= 1
            if wallloop == 0:
                wall = 0
                wallloop = 200
                print('Wall through over')

        if fast == 1:
            FPS = 10
            fastloop -= 1
            if fastloop == 0:
                print('GO FAST')
                FPS = 50
                fastloop = 50
                fast = 0

        #Check if the worm has hit itself or the edge
        if wall == 0:
            if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
                return #Game over
            for wormBody in wormCoords[1:]:
                if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                    return #game over
        else:
            if wormCoords[HEAD]['x'] == -1:
                wormCoords[HEAD]['x'] = CELLWIDTH
                direction = LEFT
            elif wormCoords[HEAD]['x'] == CELLWIDTH:
                wormCoords[HEAD]['x'] = 1
                direction = RIGHT
            elif wormCoords[HEAD]['y'] == -1:
                wormCoords[HEAD]['y'] = CELLHEIGHT
                direction = UP
            elif wormCoords[HEAD]['y'] == CELLHEIGHT:
                wormCoords[HEAD]['y'] = 1
                direction = DOWN
            for wormBody in wormCoords[1:]:
                if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                    return #game over

        #Check if worm has eaten an apple
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            #Don't remove worm's tail segment
            apple = getRandomLocation() #set new apple
        elif wormCoords[HEAD]['x'] == wallapple['x'] and wormCoords[HEAD]['y'] == wallapple['y']:
            #Don't remove worm's tail segment
            wallapple = getRandomLocation() #set new apple
            wall = 1
            print('You can go through walls!')
        elif wormCoords[HEAD]['x'] == apple3['x'] and wormCoords[HEAD]['y'] == apple3['y']:
            #Don't remove worm's tail segment
            apple3 = getRandomLocation() #set new apple
        elif wormCoords[HEAD]['x'] == greyapple['x'] and wormCoords[HEAD]['y'] == greyapple['y']:
            #Don't remove worm's tail segment
            greyapple = getRandomLocation() #set new apple
            reverse = 1
            print('Reverse started!')
        elif wormCoords[HEAD]['x'] == fastapple['x'] and wormCoords[HEAD]['y'] == fastapple['y']:
            #Don't remove worm's tail segment
            fast = 1
            print('GO SLOW')
            fastapple = getRandomLocation() #set new apple
        else:
            del wormCoords[-1] #Remove tail

        #move the worm by adding a segment in the direction it is moving
        if direction == UP:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
        wormCoords.insert(0,newHead)
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawWorm(wormCoords)
        drawApple(apple)
        drawApple(apple3)
        drawwallapple(wallapple)
        drawfastApple(fastapple)
        drawbigApple(greyapple)
        drawScore(len(wormCoords)-3,reverse,loop,wall,wallloop,fast, fastloop)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press a key to play.',True,WHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf,pressKeyRect)

def checkforKeyPress():
    if len(pygame.event.get(QUIT))>0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf',100)
    titleSurf1 = titleFont.render('Snake!',True,WHITE,DARKGREEN)
    titleSurf2 = titleFont.render('Snake!',True,GREEN)

    degrees1 = 0
    degrees2 = 0
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1,degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH/2,WINDOWHEIGHT/2)

        DISPLAYSURF.blit(rotatedSurf1,rotatedRect1)

        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOWWIDTH/2,WINDOWHEIGHT/2)

        DISPLAYSURF.blit(rotatedSurf2,rotatedRect2)

        makerSurf = BASICFONT.render('Code from inventwithpython.com, Modified by Stefan Rudvin', True, WHITE)
        makerRect = makerSurf.get_rect()
        makerRect.topleft = (30,WINDOWHEIGHT -20)
        DISPLAYSURF.blit(makerSurf,makerRect)

        drawPressKeyMsg()

        if checkforKeyPress():
            pygame.event.get() #clear event queue
            return

        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 3 #Rotate by 3 degrees each frame
        degrees2 += 7 #Rotate by 7 degrees each frame

def terminate():
    pygame.quit()
    sys.exit()

def getRandomLocation():
    return {'x':random.randint(0,CELLWIDTH - 1), 'y':random.randint(0,CELLHEIGHT - 1)}

def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf',150)
    gameSurf = gameOverFont.render('Get',True,WHITE)
    overSurf = gameOverFont.render('Rekt',True,WHITE)

    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH/2,10)
    overRect.midtop = (WINDOWWIDTH/2,gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf,gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkforKeyPress() #clear out any key presses in event queue

    while True:
        if checkforKeyPress():
            pygame.event.get() #Clear event queue
            return

def drawScore(score,reverse,loop,wall, wallloop,fast,fastloop):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 150,10)
    DISPLAYSURF.blit(scoreSurf,scoreRect)
    f = open('scores.txt', 'r')
    highscore = f.readline()
    highscore = int(highscore)
    f.close()
    if int(score) > int(highscore):
        highscore = score
        f = open('scores.txt', 'w')
        f.write(str(highscore))
        f.close()

    highscoreSurf = BASICFONT.render('Highscore: %s' % (highscore), True, WHITE)
    highscoreRect = highscoreSurf.get_rect()
    highscoreRect.topleft = (WINDOWWIDTH - 150,30)
    DISPLAYSURF.blit(highscoreSurf,highscoreRect)

    if reverse == 1:
        reverseSurf = BASICFONT.render('Reverse mode active for: ', True, WHITE)
        reverseRect = reverseSurf.get_rect()
        reverseRect.topleft = (5,35)
        DISPLAYSURF.blit(reverseSurf,reverseRect)

        reverseSurf = BASICFONT.render('%s' % (loop), True, WHITE)
        reverseRect = reverseSurf.get_rect()
        reverseRect.topleft = (240,35)
        DISPLAYSURF.blit(reverseSurf,reverseRect)

    if wall == 1:
        reverseSurf = BASICFONT.render('Wall Mode active for: ', True, WHITE)
        reverseRect = reverseSurf.get_rect()
        reverseRect.topleft = (5,10)
        DISPLAYSURF.blit(reverseSurf,reverseRect)

        reverseSurf = BASICFONT.render('%s' % (wallloop), True, WHITE)
        reverseRect = reverseSurf.get_rect()
        reverseRect.topleft = (200,10)
        DISPLAYSURF.blit(reverseSurf,reverseRect)

    if fast == 1:
        reverseSurf = BASICFONT.render('Slow Mode active for: ', True, WHITE)
        reverseRect = reverseSurf.get_rect()
        reverseRect.topleft = (5,50)
        DISPLAYSURF.blit(reverseSurf,reverseRect)

        reverseSurf = BASICFONT.render('%s' % (fastloop), True, WHITE)
        reverseRect = reverseSurf.get_rect()
        reverseRect.topleft = (200,50)
        DISPLAYSURF.blit(reverseSurf,reverseRect)

def drawWorm(wormCoords):
    for coord in wormCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        wormSegmentRect = pygame.Rect(x,y,CELLSIZE,CELLSIZE)
        pygame.draw.rect(DISPLAYSURF,DARKGREEN,wormSegmentRect)
        wormInnterSegmentRect = pygame.Rect(x+4,y+4,CELLSIZE-8,CELLSIZE - 8)

        pygame.draw.rect(DISPLAYSURF,GREEN,wormInnterSegmentRect)

def drawApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, RED, appleRect)

def drawwallapple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, BLUE, appleRect)

def drawfastApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    appleRect = pygame.Rect(x,y,CELLSIZE,CELLSIZE)
    pygame.draw.rect(DISPLAYSURF,WHITE,appleRect)

def drawbigApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    appleRect = pygame.Rect(x,y,CELLSIZE,CELLSIZE)
    pygame.draw.rect(DISPLAYSURF,DARKGRAY,appleRect)

def drawGrid():
    for x in range(0, WINDOWWIDTH,CELLSIZE): #Draw vertical lines
        pygame.draw.line(DISPLAYSURF,DARKGRAY,(x,0),(x,WINDOWHEIGHT))
    for y in range(0,WINDOWHEIGHT,CELLSIZE): #Draw horizontal lines
        pygame.draw.line(DISPLAYSURF,DARKGRAY,(0,y),(WINDOWWIDTH,y))


if __name__=='__main__':
    main(FPS)
