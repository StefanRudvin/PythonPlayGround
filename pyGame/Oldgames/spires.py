import pygame,sys,random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Sprites & Sound')

BLACK = (0,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)

basicFont = pygame.font.SysFont(None,48)

#Setup the bouncer and food data structures
foodCounter = 0
NEWFOOD = 40
player = pygame.Rect(300,100,60,40)
playerImage = pygame.image.load('Batman_logo.png')
playerStretchedImage = pygame.transform.scale(playerImage,(60,40))
foodImage = pygame.image.load('cherry.png')
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20), 20, 20))
n = 2

#Movement variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

pickUpSound = pygame.mixer.Sound('pickup.wav')
pygame.mixer.music.load('maio.mid')
pygame.mixer.music.play(-1,0.0)
musicPlaying = True

#Run the game loop
while True:
    #Check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            #Change keyboard variables
            if event.key == K_LEFT or event.key == ord('a'):
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = True
                moveLeft = False
            if event.key == K_UP or event.key == ord('w'):
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == ord('s'):
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = False
            if event.key == K_UP or event.key == ord('w'):
                moveUp = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveDown = False
            if event.key == ord('x'):
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)
            if event.key == ord('m'):
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1,0.0)
                musicPlaying = not musicPlaying

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0]-10,event.pos[1] - 10,20,20))

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        #Add new food
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20), 20, 20))

    #Draw the black background onto the surface
    windowSurface.fill(BLACK)

    #move the player
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED

    #Draw the player
    windowSurface.blit(playerStretchedImage,player)

    #Make n 0 if size is as big as the field

    if player.width == 300:
        n = 0

    #Check if the player has intersected with any food squares
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            player = pygame.Rect(player.left,player.top,player.width + n,player.height + n)

            playerStretchedImage = pygame.transform.scale(playerImage,(player.width,player.height))
            if musicPlaying:
                pickUpSound.play()

    #Draw the food
    for food in foods:
        windowSurface.blit(foodImage,food)

    #Draw the window
    pygame.display.update()
    mainClock.tick(40)
