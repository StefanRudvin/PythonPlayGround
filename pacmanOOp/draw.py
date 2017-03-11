import pygame as pg
from pygame.locals import *
import random


class Draw():
    """Draw class for OOP pacman"""

    def __init__(self):

        self._cellsize = 40
        self.size = self._width, self._height = 760, 840
        self._display_surface = None
        self._flags = pg.HWSURFACE | pg.DOUBLEBUF

        self.BGCOLOR = (0, 0, 0)
        self.DARKGRAY = (40, 40, 40)
        self.WHITE = (255, 255, 255)

        self.pointColour = (255, 255, 255)
        self.superPointColour = (255, 40, 255)
        self.playerColour = (0, 255, 255)
        self.ghostColour = (255, 255, 255)
        self.wallColour = (40, 40, 40)

        pg.init()
        self._display_surface = pg.display.set_mode(self.size, self._flags)
        pg.display.set_caption("Pacman")

        print("Draw class initialized.")

    def update(self, pg):
        self._display_surface.fill(self.BGCOLOR)
        self.drawGrid(pg)

    def drawGrid(self, pg):
        for x in range(0, self._width, self._cellsize):
            pg.draw.line(self._display_surface,
                         self.DARKGRAY, (x, 0), (x, self._height))

        for y in range(0, self._height, self._cellsize):
            pg.draw.line(self._display_surface,
                         self.DARKGRAY, (0, y), (self._width, y))
        pass

    def drawWalls(self, wall):
        for i, (x, y) in enumerate(wall):
            self.drawRect(*self.convertToPixel(*wall[i]), self.wallColour)

    def drawPoints(self, p):
        for i, (x, y) in enumerate(p):
            self.drawHalfRect(*self.convertToPixel(*p[i]), self.pointColour)

    def drawSuperPoints(self, p):
        for i, (x, y) in enumerate(p):
            self.drawHalfRect(*self.convertToPixel(*p[i]), (random.randint(200, 250), 40, 40))

    def colourRange(self):
        return

    def drawPlayer(self, playerPos):
        self.drawPlayerRects(*self.convertToPixel(*playerPos))

    def drawPlayerRects(self, x, y):
        i = self._cellsize
        b = i / 10
        self.drawMyRect(x, y, b, b + 20, b)
        self.drawMyRect(x, y, b, b + 28, b)
        self.drawMyRect(x, y, b + 5, b + 20, b)
        self.drawMyRect(x, y, b, b + 20, b)
        self.drawMyRect(x, y, b + 10, b + 20, b)
        self.drawMyRect(x, y, b + 25, b + 20, b)
        self.drawMyRect(x, y, b + 20, b, b)
        self.drawMyRect(x, y, b + 20, b + 20, b)

    def drawMyRect(self, x, y, a, b, c):
        pg.draw.rect(self._display_surface, self.DARKGRAY,
                     (x + a, y + b, c, c), 0)
        pg.draw.rect(self._display_surface, self.WHITE,
                     (x + a, y + b, c, c), 2)

    def drawGhosts(self, i):
        for a, b in enumerate(i):
            self.drawRect(*self.convertToPixel(b[0], b[1]), self.ghostColour)

    def drawRect(self, x, y, colour):
        i = self._cellsize
        pg.draw.rect(self._display_surface, colour, (x, y, i, i), 0)
        pg.draw.rect(self._display_surface, self.WHITE, (x, y, i, i), 2)

    def drawHalfRect(self, x, y, colour):
        i = self._cellsize
        b = i / 3
        pg.draw.rect(self._display_surface, colour, (x + b, y + b, b, b), 0)
        pg.draw.rect(self._display_surface, self.WHITE,
                     (x + b, y + b, b, b), 2)

    def convertToPixel(self, x, y):
        return int(x * self._cellsize), int(y * self._cellsize)

    def _get_half_width(self):
        return self._width / 2

    def _get_half_height(self):
        return self._height / 2
