import sys
import pygame as pg
from pygame.locals import *
import mapGen
import random
from draw import Draw
from player import Player
from ghost import Ghost
from collision import Collision

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
        self._clock = pg.time.Clock()
        self.FPS = 10

        self.playerPos = (0, 0)
        self.ghostPos = []
        self.walls = []
        self.superPoints = []
        self.points = []
        self.score = 0

    def on_init(self):

        # Initialize level
        level = mapGen.Map()
        self.level = level.getLevel()
        level.makeLevelVariables()

        # Initialize Draw class
        self.draw = Draw()

        # Get variables from .txt
        self.playerPos = level.playerPos
        self.ghostPos = level.ghosts
        self.walls = level.walls
        self.superPoints = level.superpoints
        self.points = level.points
        self._running = True

        # Initialize player class
        self.player = Player(self.playerPos, self.walls)

        # Initialize Ghost class
        self.ghost1 = Ghost(self.playerPos, self.ghostPos[0], self.walls)

        # Initialize Collision class
        self.collision = Collision()

    def on_event(self, event):
        if event.type == QUIT or \
           (event.type == KEYUP and event.key == K_ESCAPE):
            self._running = False

        self.player.userInput(event)  # Make moveVert etc.

    def on_loop(self, events):
        # TODO: on loop events. Takes in pygame events.

        self.playerPos = self.player.movePlayer()

        # Update collision class
        self.collision.update(self.points, self.playerPos, self.superPoints)

        # Get variables
        self.score = self.collision.score
        self.points = self.collision.points
        self.superPoints = self.collision.superPoints

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
