from pygame.locals import *

# Player class for pacmanOOP.
# Handles keyboard input & blocking.
# Returns players next move based on events.


class Player():

    def __init__(self, playerPos, walls):
        self.playerPos = playerPos

        self.moveHor = 0
        self.moveVert = 0
        self.walls = walls

        print("Player class initialized.")

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

    def movePlayer(self):
        x = self.playerPos
        h = self.moveHor
        v = self.moveVert

        if h != 0:
            if h == 1:
                x = (x[0] + 1, x[1])
            elif h == -1:
                x = (x[0] - 1, x[1])
            h = 0
        elif v != 0:
            if v == 1:
                x = (x[0], x[1] - 1)
            elif v == -1:
                x = (x[0], x[1] + 1)
            v = 0

        if not self.isBlocked(x[0], x[1]):
            if x[0] < 0:
                x = (18, x[1])
            elif x[0] > 18:
                x = (0, x[1])
            self.playerPos = x

        self.moveHor = h
        self.moveVert = v

        return self.playerPos

    def isBlocked(self, x, y):
        if [x, y] in self.walls:
            print("Blocked!")
            return True
