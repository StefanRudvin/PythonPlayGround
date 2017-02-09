# Ghost class for OOP Pacman
from player import Player


class Ghost(object):

    """docstring for Ghost"""

    def __init__(self, playerPos, ghostPos, walls):
        self.walls = walls
        self.playerPos = playerPos
        self.ghostPos = ghostPos

        print("Ghost class initialized.")
        # print("Ghost initial position: ", self.ghostPos)

    def moveGhost(self, playerPos, ghostPos):
        self.playerPos = playerPos
        self.ghostPos = ghostPos

    def makeNodes(self):

        # Witdth: 18
        # Height: 20
        pass
        # Make nodes

        # remember you can call Player.isBlocked(x, y)
