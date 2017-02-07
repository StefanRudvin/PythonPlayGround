import sys
import pygame as pg
from pygame.locals import *
import mapGen

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
        self.size = self._width, self._height = 840, 760

        self.FPS = 30
        self.BGCOLOR = (0, 0, 0)
        self.DARKGRAY = (40, 40, 40)
        self.WHITE = (255, 255 ,255)
        self.moveVert = 0
        self.moveHor = 0

        self.playerPos = (0, 0)
        self.ghostPos = []
        self.walls = []
        self.superPoints = []

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
        level.getLevel()
        level.makeLevelVariables()

        self.playerPos = level.getInitialPlayerPos()
        self.ghostPos = level.getGhostInitialPos()
        self.walls = level.getWalls()
        self.superpoints = level.getSuperPoints()
        self.level = level.getLevel()
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
                self.moveVert = -1
            elif (event.key == K_RIGHT or
                  event.key == K_d) and self.moveHor == 0:
                self.moveVert = 1
            elif (event.key == K_UP or
                  event.key == K_w) and self.moveVert == 0:
                self.moveHor = 1
            elif (event.key == K_DOWN or
                  event.key == K_s) and self.moveVert == 0:
                self.moveHor = -1
            print("Vertical: ", self.moveVert)
            print("Horizontal: ", self.moveHor)
        elif event.type == KEYUP:
            if (event.key == K_LEFT or event.key == K_a):
                self.moveVert = 0
            elif (event.key == K_RIGHT or event.key == K_d):
                self.moveVert = 0
            elif (event.key == K_UP or event.key == K_w):
                self.moveHor = 0
            elif (event.key == K_DOWN or event.key == K_s):
                self.moveHor = 0

    def on_loop(self, events):
        # TODO: on loop events. Takes in pygame events.
        pass

    def drawGrid(self):
        for x in range(0, self._width, self._cellsize):
            pg.draw.line(self._display_surface,
                         self.DARKGRAY, (x, 0), (x, self._height))

        for y in range(0, self._height, self._cellsize):
            pg.draw.line(self._display_surface,
                         self.DARKGRAY, (0, y), (self._width, y))
        pass

    def drawMap(self):
        i = self.walls
        for x in range(len(i)):
            self.drawRect(*self.convertToPixel(i[x][0], i[x][1]), self.DARKGRAY)

    def drawPlayer(self):
        self.drawRect(*self.convertToPixel(*self.playerPos), self.WHITE)
        pass

    def drawGhosts(self):
        i = self.ghostPos
        for a, b in enumerate(i):
            self.drawRect(*self.convertToPixel(b[0],b[1]), self.WHITE)

    def convertToPixel(self, x, y):
        return int(x * self._cellsize), int(y * self._cellsize)

    def drawRect(self, x, y, colour):
        i = self._cellsize
        pg.draw.rect(self._display_surface, colour, (x, y, i, i), 0)  # Inner
        pg.draw.rect(self._display_surface, self.WHITE, (x, y, i, i), 2)  # Outer

    def on_render(self):
        self._display_surface.fill(self.BGCOLOR)
        # Add rendering events here
        # pygame.display.update()
        self.drawGrid()
        self.drawMap()
        self.drawPlayer()
        self.drawGhosts()
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


class Player():

    def __init__(self, playerPos):
        self.playerPos = playerPos


if __name__ == '__main__':
    app = Game()
    app.run()
