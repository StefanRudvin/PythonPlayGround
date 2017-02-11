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

    # Heuristics function takes 2 tuples of inputs, finds the heuristic distance between them.
    def heuristic(a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)

    def a_star_search(graph, start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break # Found the goal

            for (x,y) in isNeighbour(current,graph):
                new_cost = cost_so_far[current] + cost(current, (x,y))

                if (x,y) not in cost_so_far or new_cost < cost_so_far[x,y]:
                    # If next (x,y) that isNeighbours provides is not in the dictionary of (x,y + cost) of past locations
                    # OR
                    # The newcost
                    cost_so_far[x,y] = new_cost
                    priority = new_cost + heuristic(goal, (x,y))
                    frontier.put((x,y), priority)
                    came_from[x,y] = current

        #return came_from, cost_so_far
        return frontier.get()
