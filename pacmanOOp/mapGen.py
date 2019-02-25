import os


class Map():
    """This class opens Level.txt, creates an array out of it and variables for
    player, ghost, walls, points, superpoints. Also provides getter functions for
    each of the previous."""

    def __init__(self):
        self._filename = "Level.txt"
        self.level = []
        self.playerPos = (0, 0)
        self.ghosts = []
        self.walls = []
        self.points = []
        self.superpoints = []

        print("MapGen class initialized.")

    def getLevel(self):
        assert os.path.exists(
            self._filename), 'Cant find the level file: %s' % (self._filename)
        mapFile = open(self._filename, 'r')
        content = mapFile.readlines() + ['\r\n']
        mapFile.close()

        level = []
        mapObj = []

        for linenum in range(len(content)):
            line = content[linenum].rstrip('\r\n')

            if line != '':
                level.append(line)

        for x in range(len(level[0])):
            mapObj.append([])
        for y in range(len(level)):
            for x in range(len(level[0])):
                mapObj[x].append(level[y][x])

        self.level = mapObj

    def makeLevelVariables(self):

        self.getLevel()

        for x in range(len(self.level)):
            for y in range(len(self.level[0])):
                point = self.level[x][y]
                if point == "#":
                    self.walls.append([x, y])
                elif point == "@":
                    self.playerPos = (x, y)
                elif point == "1":
                    self.ghosts.append([x, y])
                elif point == "o":
                    self.points.append([x, y])
                elif point == "z":
                    self.superpoints.append([x, y])
