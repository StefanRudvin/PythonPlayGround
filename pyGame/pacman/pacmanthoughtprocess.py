'''
Pacman game
Variables and shit
Main()
    Starts game Variables
    startScreen()
    Keeps level variable
    readLevelsFile() with current level
    loops the runLevel() function, with levels.
    waits for the return of the level function, then change level accordingly.

runLevel()
    make map with previous levels file and decorateMap()
    This makes the Level with pacman position, walls, goals and ghosts.
    Set level number text on bottom left of screen
    Render map with tilewidth
    Track camera movement- CameraXpan etc, I won't need that.
    Loop per FPS, so like a lot of times:
        playerMoveTo = False
        keyPressed = False
        Get INPUT
            if KEYDOWN:
                keyPressed = True
                playerMoveTo = direction of player & Map
                change pacman colour and shit
            if KEYUP:
                stop camera movement
        if move is asserted and levelnotcomplete:
            movePlayer, checking for walls etc
            if move successful:
                steps += 1
                redraw map
            if levelIsFinished():
                # Level is complete, show the "Finished screen"
                levelIsComplete = True
                keyPressed = False
        fill BGCOLOR

        if mapNeedsRedraw():
            redraw map
            mapNeedsRedraw = False

        if moveCamera:
            move the camera!!

        Draw the DISPLAYSURF, center the camera with new offsetX and Y. with HALF_WINWIDTH

        DISPLAYSURF.blit

        if levelIsComplete:
            solvedRect = Dict[solved].get_rect
            center to normal half widths

            if keyPressed:
                return'solved'

        # Game not completed,
        pygame.display.update()
        FPSCLOCK.tick()

'''
print("Pacman Game")
'''
- Communicate from makeMove to runLevel to Main that ghost Touched

- Ghost has touched, lives work etc yayy!!

Make points work:
Communicate points via mapObj NOT gameStateObj
all 'inside floors' are points that must be collected.

First info is taken out with readLevel()

decorateMap() changes everything but game aspects.

Then game is drawn with x,y coordinates
for each coordinate:
    if in tilemapping:
        if inside:
            draw that shit
        if outside:
            draw the outside shit

        if foliage:
            draw trees and shit
        else if stars:
            if on goal:   ### IF ON BOTH GOAL AND STARS
                draw goal
            draw star
        else if goal:

If i draw on the shit:
it messes up:
flashfill (inside and outisde shit)
corners

add it later?? Add to gameStateObj after decorateMap?

write back to it line by line?

Next: Collision
If player hits point or superPoint, delete it from mapObj

deleting from list of lists

if you delete the value, the next value shows up

x 0, y 9

x 18 y 9

Change these!
Make a new function for them?
I think so!
to change

ghost mechanics:
specify the point where the ghost wants to go to.
Collision is done already
Ghost looks at "path"? idk how
It makes a graph of the whole thing with


Like a flashfill that goes through the entire map.

frontier = Queue()
frontier.put(start )
came_from = {}
came_from[start] = None

while not frontier.empty():
   current = frontier.get()

   if current == goal:
      break

   for next in graph.neighbors(current):
      if next not in came_from:
         frontier.put(next)
         came_from[next] = current


Go through neighbours one by one, then putting them into the came_from list which will not be counted in the future.

For this we need the frontier class with: Queue(), .put (star), .get() for the current, put() to put it into the class.

We can also put cost per movement so that specific points on the map become harder to move in, and the algorithm takes that into account.

Taking costs into account going through the options is different, as it 'goes around' slow spots and finds the fastest way to the goal.

All of the methods above, the frontier expands in all directions. This is useful for finding all paths to many locations, but usually you're trying to find a single spot.

With heuristics we can make the next be the value from a breadthfirst search, which finds the closest path to the goal.

The A* uses both the actual distance from the start and the estimated distance to the goal.

frontier = PriorityQueue()
frontier.put(start, 0)
came_from = {}
cost_so_far = {}
came_from[start] = None
cost_so_far[start] = 0

while not frontier.empty():
   current = frontier.get()

   if current == goal:
      break

   for next in graph.neighbors(current):
      new_cost = cost_so_far[current] + graph.cost(current, next)
      if next not in cost_so_far or new_cost < cost_so_far[next]:
         cost_so_far[next] = new_cost
         priority = new_cost + heuristic(goal, next)
         frontier.put(next, priority)
         came_from[next] = current

A* Finds an optimal path to the goal. It uses heuristics to find that the next node is more likely to be found sooner.

Make the mapObj() with empty spots or stars (0) for movement for the ghost.

a function called neightbour():

def neighbors(node):
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for dir in dirs:  # for [1,0]
        neighbor = [node[0] + dir[0], node[1] + dir[1]]
        if neighbor in all_nodes: # All nodes holds all possible values (exclude the others!!)
            result.append(neighbor)
    return result

returns each neighbour for the selected node.

for obstacles you can either remove the node (then you have to remove the corresponding edges, which happens automatically if you're using if neighbour in all_nodes), remove the edge  (check this in neighbours), or you can set the edge weight as infinity.


------------- Breath first algorithm -------------------

Pacman game to demonstrate breadth first, best first and A* algorithms.
Different levels for different algorithms? Like select a for that. That would be awesome!!

- Graph data structure with neighbour() function
- Locations (x,y) tuples which labels locations on the graph.
- Search: algorithm that takes starting position, optional goal location, and calculates visited, parent pointer, distance for some or all locations.
- Queue: data structure used by algorithm to determine the order in which to process locations.
