# Collision class for OOP Pacman.

# Takes playerPos, points and superPoints
# Updates point score

class Collision():
    """docstring for collision."""
    def __init__(self):
        print("Collision class initialized.")
        self.score = 0

    def update(self, points, playerPos, superPoints):
        self.points = points
        self.superPoints = superPoints
        self.playerPos = playerPos

        for i, (j, k) in enumerate(points):
            if (playerPos[0], playerPos[1]) == (j, k):
                del self.points[i]
                self.score += 1

        for i, (j, k) in enumerate(superPoints):
            if (playerPos[0], playerPos[1]) == (j, k):
                del self.superPoints[i]
                self.score += 1
