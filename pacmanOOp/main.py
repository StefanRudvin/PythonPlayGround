import sys
import pygame as pg
from pygame.locals import *
import level
import random
from draw import Draw
from player import Player
from ghost import Ghost
from collision import Collision

class Game:

    def __init__(self):
        self._running = True
        self._clock = pg.time.Clock()
        self.FPS = 10

        self.ghostPos = []
        self.score = 0

    def on_init(self):

        # Initialize level. Level class contains walls, points and superpoints
        self.level = level.Map()
        self.level.make_level_variables()

        # Initialize Draw class
        self.draw = Draw()

        # Get player and ghost variables from level class
        self.playerPos = self.level.playerPos
        self.ghostPos = self.level.ghosts

        self._running = True

        # Initialize player class
        self.player = Player(self.playerPos, self.level.walls)

        # Initialize Ghost class
        self.ghost1 = Ghost(self.ghostPos[0], self.level.walls)

        # Initialize Collision class
        self.collision = Collision()

    def on_event(self, event):
        if event.type == QUIT or \
           (event.type == KEYUP and event.key == K_ESCAPE):
            self._running = False

        self.player.user_input(event)  # Make moveVert etc.

    def on_loop(self, events):
        # TODO: on loop events. Takes in pygame events.

        self.playerPos = self.player.movePlayer()

        self.ghostPos[0] = self.ghost1.moveGhost(self.playerPos, self.ghostPos[0])

        # Update collision class
        self.collision.update(self.level.points, self.playerPos, self.level.superpoints, self.ghostPos)

        # Get variables
        self.score = self.collision.score
        self.level.points = self.collision.points
        self.level.superpoints = self.collision.superPoints

    def on_render(self):
        # Draw() class renders everything.
        self.draw.update(pg)
        self.draw.draw_walls(self.level.walls)
        self.draw.draw_points(self.level.points)
        self.draw.draw_super_points(self.level.superpoints)
        self.draw.draw_player(self.playerPos)
        self.draw.draw_ghosts(self.ghostPos)

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
