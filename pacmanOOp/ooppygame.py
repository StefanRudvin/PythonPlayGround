import sys
import pygame as pg
from pygame.locals import *
import mapGen
import player
import random

# Colours
# Add colours here instead of __init__

# Task list:
'''
- colours
- key input
- player class
- ghost class
- ai


'''

class Game:

    def __init__(self):
        self._running = True
        self._display_surface = None
        self._clock = pg.time.Clock()
        self._flags = pg.HWSURFACE | pg.DOUBLEBUF
        self._cellsize = 40
        self.size = self._width, self._height = 760, 840

        self.FPS = 5
        self.BGCOLOR = (0, 0, 0)
        self.DARKGRAY = (40, 40, 40)
        self.WHITE = (255, 255 ,255)
        self.moveVert = 0
        self.moveHor = 0

        self.pointColour = (255, 255 ,255)
        self.superPointColour = (255, 40 ,255)
        self.playerColour = (0, 255 ,255)
        self.ghostColour = (255, 255 ,255)
        self.wallColour = (40, 40, 40)


        self.playerPos = (0, 0)
        self.ghostPos = []
        self.walls = []
        self.superPoints = []
        self.points = []

    def _get_half_width(self):
        return self._width / 2

    def _get_half_height(self):
        return self._height / 2

    def on_init(self):
        pg.init()
        self._display_surface = pg.display.set_mode(self.size, self._flags)
        pg.display.set_caption("Pacman")

        # Initialize level
        level = mapGen.Map()
        self.level = level.getLevel()
        level.makeLevelVariables()

        # Initialize variables
        self.playerPos = level.getInitialPlayerPos()
        print("This should only print once")

        self.ghostPos = level.getGhostInitialPos()
        self.walls = level.getWalls()
        self.superPoints = level.getSuperPoints()
        self.points = level.getPoints()
        self._running = True

        print("Player pcos: ", self.playerPos)
        print("Ghost pos: ", self.ghostPos)
        #print("Walls: ", self.walls)

    def on_event(self, event):
        if event.type == QUIT or \
           (event.type == KEYUP and event.key == K_ESCAPE):
            self._running = False

        self.userInput(event)  # Make moveVert etc.

    def userInput(self, event):
        # Process key inputs. To be rarefactored.
        if event.type == KEYDOWN:
            if (event.key == K_LEFT or event.key == K_a) and self.moveHor == 0:
                self.moveHor = -1
                self.moveVert = 0
            elif (event.key == K_RIGHT or
                  event.key == K_d) and self.moveHor == 0:
                self.moveHor = 1
                self.moveVert = 0

            elif (event.key == K_UP or
                  event.key == K_w) and self.moveVert == 0:
                self.moveVert = 1
                self.moveHor = 0
            elif (event.key == K_DOWN or
                  event.key == K_s) and self.moveVert == 0:
                self.moveVert = -1
                self.moveHor = 0
            print("Vertical: ", self.moveVert)
            print("Horizontal: ", self.moveHor)
            print("Player pcos: ", self.playerPos)
        # elif event.type == KEYUP:
        #     if (event.key == K_LEFT or event.key == K_a):
        #         self.moveHor = 0
        #         print("Stopped going left")
        #     elif (event.key == K_RIGHT or event.key == K_d):
        #         self.moveHor = 0
        #     elif (event.key == K_UP or event.key == K_w):
        #         self.moveVert = 0
        #     elif (event.key == K_DOWN or event.key == K_s):
        #         self.moveVert = 0

    def on_loop(self, events):
        # TODO: on loop events. Takes in pygame events.
        self.movePlayer()
        self.checkPointCollision()
        pass

    def checkPointCollision(self):

        for i, (j, k) in enumerate(self.points):
            if (self.playerPos[0], self.playerPos[1]) == (j, k):
                del self.points[i]

    def movePlayer(self):
        x = self.playerPos
        h = self.moveHor
        v = self.moveVert

        # if h == 1:
        #     x = (x[0] + 1,x[1])
        # elif h == -1:
        #     x = (x[0] - 1,x[1])
        # elif v == 1:
        #     x = (x[0],x[1] - 1)
        # elif v == -1:
        #     x = (x[0],x[1] + 1)

        if h != 0:
            if h == 1:
                x = (x[0] + 1,x[1])
            elif h == -1:
                x = (x[0] - 1,x[1])
            h = 0
        elif v != 0:
            if v == 1:
                x = (x[0],x[1] - 1)
            elif v == -1:
                x = (x[0],x[1] + 1)
            v = 0

        if not self.isBlocked(x[0], x[1]):
            self.playerPos = x
        self.moveHor = h
        self.moveVert = v

    def isBlocked(self, x, y):
        if [x, y] in self.walls:
            print("Blocked!")
            return True


    def on_render(self):
        self._display_surface.fill(self.BGCOLOR)
        # Add rendering events here
        # pygame.display.update()
        pg.transform.rotate(self._display_surface, 90)

        self.drawGrid()
        self.drawWalls()
        self.drawPoints()
        self.drawSuperPoints()
        self.drawPlayer()
        self.drawGhosts()
        self.drawRect(*self.convertToPixel(2,3),self.WHITE)
        pg.display.flip()

    def on_terminate(self):
        pg.quit()
        sys.exit()

    def run(self):
        if self.on_init() is False:
            self._running = False

        while self._running:
            self._clock.tick(self.FPS)

            filtered_events = []
            for event in pg.event.get():
                self.on_event(event)
                if self._running:
                    filtered_events.append(event)
            self.on_loop(filtered_events)
            self.on_render()
        self.on_terminate()

    def drawGrid(self):
        for x in range(0, self._width, self._cellsize):
            pg.draw.line(self._display_surface,
                         self.DARKGRAY, (x, 0), (x, self._height))

        for y in range(0, self._height, self._cellsize):
            pg.draw.line(self._display_surface,
                         self.DARKGRAY, (0, y), (self._width, y))
        pass

    def drawWalls(self):
        wall = self.walls
        for i, (x, y) in enumerate(wall):
            self.drawRect(*self.convertToPixel(*wall[i]), self.wallColour)

    def drawPoints(self):
        p = self.points
        for i, (x, y) in enumerate(p):
            self.drawHalfRect(*self.convertToPixel(*p[i]), self.pointColour)

    def drawSuperPoints(self):
        p = self.superPoints
        for i, (x, y) in enumerate(p):
            self.drawHalfRect(*self.convertToPixel(*p[i]), (random.randint(200, 250), 40,40))

    def colourRange(self):
        return

    def drawPlayer(self):
        self.drawRect(*self.convertToPixel(*self.playerPos), self.playerColour)

    def drawGhosts(self):
        i = self.ghostPos
        for a, b in enumerate(i):
            self.drawRect(*self.convertToPixel(b[0],b[1]), self.ghostColour)

    def drawRect(self, x, y, colour):
        i = self._cellsize
        pg.draw.rect(self._display_surface, colour, (x, y, i, i), 0)
        pg.draw.rect(self._display_surface, self.WHITE, (x, y, i, i), 2)

    def drawHalfRect(self, x, y, colour):
        i = self._cellsize
        b = i/3
        pg.draw.rect(self._display_surface, colour, (x+b, y+b, b, b), 0)
        pg.draw.rect(self._display_surface, self.WHITE, (x+b, y+b, b, b), 2)

    def convertToPixel(self, x, y):
        return int(x * self._cellsize), int(y * self._cellsize)



if __name__ == '__main__':
    app = Game()
    app.run()
