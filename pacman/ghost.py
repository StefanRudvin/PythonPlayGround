import heapq
''' gameStateObj contains player, stepcounter, stars, ghosts, points and superPoints
mapObj contains the mapitself.
'''

# Get the direction of movement and move ghost to direction.
# Checks are made earlier.

def makeGhostMove(mapObject, gameObj):
    playerx, playery = gameObj['player']
    ghostx = gameObj['ghosts'][0][0]
    ghosty = gameObj['ghosts'][0][1]

    # mapObject is a list of lists.
    # One list per line.
    # Find it's neighbours?

    graph = mapObject
    start = (ghostx,ghosty)
    neighbors = isNeighbour(start,graph)

    #print("Ghost position: ",gameObj["ghosts"],"Next position: ",a_star_search(graph,(ghostx,ghosty),(playerx,playery)))

    #print(isNeighbour(gameObj['ghosts'][0],graph))
    return mySearch(graph,(ghostx,ghosty),(playerx,playery))

    '''
    A star takes in: neighbours, playerx, playery, ghostx, ghosy AND mapObject.

    It must:

    1. Look at the possible neighbours
    2. Select the neighbouring that is (x,y) closest to playerx, playery.
    '''

    # Return the next step to move to.
    #return neighbors[0]

def mySearch(graph,ghost,goal):

    # Cycle through neighbours
    # Find which one is closest to

    points = heuristic(goal,ghost)

    for (x,y) in isNeighbour(ghost,graph):
        if heuristic(goal,(x,y)) < points:
            return (x,y)


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


def isNeighbour(node, mapObj):
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for dir in dirs:
        neighbor = [node[0] + dir[0],node[1] + dir[1]]
        if not isWall(mapObj,neighbor[0],neighbor[1]):
            result.append(neighbor)

    return result

# Heuristics function takes 2 tuples of inputs, finds the heuristic distance between them.
def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def cost(currentplace,next):
    return 10

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

def isWall(mapObj, x, y):
    """Returns True if the (x, y) position on
    the map is a wall, otherwise return False."""
    if x < 0 or x >= len(mapObj) or y < 0 or y >= len(mapObj[x]):
        return False # x and y aren't actually on the map.
    elif mapObj[x][y] in ('#', 'x'):
        return True # wall is blocking
    return False

class graph:
    def __init__(self):
        self.edges = {}

    def isNeighbour(node, mapObj):
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        result = []
        for dir in dirs:
            neighbor = [node[0] + dir[0], node[1] + dir[1]]
            if not isWall(mapObj,neighbor[0],neighbor[1]):
                result.append(neighbor)
        return result
