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
