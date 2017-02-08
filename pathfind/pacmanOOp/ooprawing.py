import sys
import pygame as pg
from pygame.locals import *
import mapGen
import random
from draw import Draw
from player import Player

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

        self.FPS = 10
        self.moveVert = 0
        self.moveHor = 0

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

        # Initialize Draw class
        self.draw = Draw(self._display_surface, self._cellsize,
                         self._width, self._height)

        # Get variables from .txt
        self.playerPos = level.getInitialPlayerPos()
        self.ghostPos = level.getGhostInitialPos()
        self.walls = level.getWalls()
        self.superPoints = level.getSuperPoints()
        self.points = level.getPoints()
        self._running = True

        # Initialize player class
        self.player = Player(self.playerPos, self.walls)

    def on_event(self, event):
        if event.type == QUIT or \
           (event.type == KEYUP and event.key == K_ESCAPE):
            self._running = False

        self.player.userInput(event)  # Make moveVert etc.

    def on_loop(self, events):
        # TODO: on loop events. Takes in pygame events.

        self.playerPos = self.player.movePlayer()

        self.checkPointCollision()

    def checkPointCollision(self):
        for i, (j, k) in enumerate(self.points):
            if (self.playerPos[0], self.playerPos[1]) == (j, k):
                del self.points[i]

    def on_render(self):
        # Draw() class renders everything.
        self.draw.update(pg)
        self.draw.drawWalls(self.walls)
        self.draw.drawPoints(self.points)
        self.draw.drawSuperPoints(self.superPoints)
        self.draw.drawPlayer(self.playerPos)
        self.draw.drawGhosts(self.ghostPos)

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


if __name__ == '__main__':
    app = Game()
    app.run()
