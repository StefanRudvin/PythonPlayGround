# Ghost class for OOP Pacman
from player import Player


class Ghost(object):

    def __init__(self, ghostPos, walls):    
        self.walls = walls
        self.ghostPos = ghostPos
        self.nodes = self.makeNodes()
        self.found = 0
        self.visited = []

        print("Ghost class initialized.")

    def moveGhost(self, playerPos, ghostPos):
        self.bruteforce(ghostPos, playerPos)

        print(self.nodes)

        return ghostPos

    def bruteforce(self, ghostPos, playerPos):
        if self.found < 600:
            (a, b) = ghostPos
            self.visited.append((a,b))
            self.found += 1
            if self.found > 5:
                pass
                del self.visited[0]
            if (a, b) == playerPos:
                self.found = 500
            if (a + 1, b) in self.nodes and (a+1, b) not in self.visited:
                self.bruteforce((a + 1, b), playerPos)
            if (a - 1, b) in self.nodes and (a-1, b) not in self.visited:
                self.bruteforce((a - 1, b), playerPos)
            if (a, b + 1) in self.nodes and (a, b+1) not in self.visited:
                self.bruteforce((a, b + 1), playerPos)
            if (a, b - 1) in self.nodes and (a, b-1) not in self.visited:
                self.bruteforce((a, b - 1), playerPos)




    def makeNodes(self):
        # Witdth: 18 Height: 20
        ar = []
        for x in range(18):
            for y in range(20):
                if [x, y] not in self.walls:
                    ar.append((x, y))
        return ar

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
