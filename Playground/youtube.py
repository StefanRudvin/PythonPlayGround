import pygame
import time

pygame.init()

display_width = 800
display_height = 600

#               R    G    B
WHITE = (255, 255, 255)
GRAY = (185, 185, 185)
BLACK = (0, 0, 0)
RED = (155, 0, 0)
LIGHTRED = (175, 20, 20)
GREEN = (0, 155, 0)
LIGHTGREEN = (20, 175, 20)
BLUE = (0, 0, 155)
LIGHTBLUE = (20, 20, 175)
YELLOW = (155, 155, 0)
LIGHTYELLOW = (175, 175, 20)

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('A bit racey')

clock = pygame.time.Clock()
FPS = 30

carImg = pygame.image.load('car.png').convert_alpha()


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


x = (display_width * 0.45)
y = (display_height * 0.8)

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(WHITE)

    car(x, y)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
