# Stay pusher from inventwithPython

import random, sys, copy, os, pygame
from pygame.locals import *

FPS = 30
WINWIDTH = 800 # Width of the program window in pixels
WINHEIGHT = 600 # Height in pixels
HALF_WINWIDTH = int(WINWIDTH/2)
HALF_WINHEIGHT = int(WINHEIGHT/2)

# The total width and height for each tile in pixels.
TILEWIDTH = 50
TILEHEIGHT = 85
TILEFLOORHEIGHT = 40

CAM_MOVE_SPEED = 5 # how many pixels per frame the camera moves

# The percentage of outdoor tiles that have additional
#Decoration of them, like a tree or a rock
OUTSIDE_DECORATION_PCT = 20

BRIGHTBLUE = (0, 170, 255)
WHITE = (255,255,255)
BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def main():
    global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, OUTSIDEDECOMAPPING, BASICFONT, PLAYERIMAGES, currentImage

    #Pygame initialization and basic setup of the global variables
    pygame.init()
    FPSCLOCK = pygame.time.Clock()

    #Because the Surface object stored in DISPLAYSURF was returned
    #from the pygame.display.set_mode() function, this is the surface object that is drawn to the actual computer screen
    #When the pygame.display.update() is called.
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH,WINHEIGHT))

    pygame.display.set_caption('Star Pusher')
    BASICFONT = pygame.font.Font('freesansbold.ttf',18)

    # A global dict value that will contain all the pygame Surface objects returned by pygame.image.load()

    IMAGESDICT = {'uncovered goal': pygame.image.load('RedSelector.png'),
            'covered goal': pygame.image.load('Selector.png'),
            'star': pygame.image.load('Star.png'),
            'corner': pygame.image.load('Wall_Block_Tall.png'),
            'wall': pygame.image.load('Wood_Block_Tall.png'),
            'inside floor': pygame.image.load('Plain_Block.png'),
            'outside floor': pygame.image.load('Grass_Block.png'),
            'title': pygame.image.load('star_title.png'),
            'solved': pygame.image.load('star_solved.png'),
            'princess': pygame.image.load('princess.png'),
            'boy': pygame.image.load('boy.png'),
            'catgirl': pygame.image.load('catgirl.png'),
            'horngirl': pygame.image.load('horngirl.png'),
            'pinkgirl': pygame.image.load('pinkgirl.png'),
            'rock': pygame.image.load('Rock.png'),
            'short tree': pygame.image.load('Tree_Short.png'),
            'tall tree': pygame.image.load('Tree_Tall.png'),
            'ugly tree': pygame.image.load('Tree_Ugly.png')}

    #These dict values are global, and map the character that appears in the level file to the Surface object it represents
    TILEMAPPING = {'x':IMAGESDICT['corner'],
                '#':IMAGESDICT['wall'],
                'o':IMAGESDICT['inside floor'],
                '':IMAGESDICT['outside floor']}
    OUTSIDEDECOMAPPING = {'1': IMAGESDICT['rock'],
                        '2': IMAGESDICT['short tree'],
                        '3': IMAGESDICT['tall tree'],
                        '4': IMAGESDICT['ugly tree']}

    #PLAYERIMAGES is a list of all possible characters the player can be.
    #currentImage is the index of the players current image.
    currentImage = 0
    PLAYERIMAGES = [IMAGESDICT['princess'],
                    IMAGESDICT['boy'],
                    IMAGESDICT['catgirl'],
                    IMAGESDICT['horngirl'],
                    IMAGESDICT['pinkgirl']]
    print("before startscreen is called")
    startScreen() # Show the title screen until the user presses a key

    # Read in the levels from the text tile. See the readLevelsFile() for details on the format and how to make own levels
    levels = readLevelsFile('starPusherLevels.txt')
    currentLevelIndex = 0

    # Main game loop. runs a single level, when user finishes level. Then next level is loaded
    while True: # Main gameloop
        #Run the level to actually start playing the game
        result = runLevel(levels,currentLevelIndex)

        if result in ('solved','next'):
            #Go to next level
            currentLevelIndex += 1
            if currentLevelIndex >= len(levels):
                # No more levels, go back to first one
                currentLevelIndex = 0
        elif result == 'back':
            currentLevelIndex -= 1
            if currentLevelIndex < 0:
                #If there are no previous levels, go to the last one
                currentLevelIndex = len(levels) -1
        elif result == 'reset':
            pass # do nothing. loop recalls runLevel to reset level.

def runLevel(levels, levelNum):
    global currentImage
    levelObj = levels[levelNum]
    mapObj = decorateMap(levelObj['mapObj'], levelObj['startState']['player'])
    gameStateObj = copy.deepcopy(levelObj['startState'])
    mapNeedsRedraw = True # set to True to call drawMap()
    levelSurf = BASICFONT.render('Level %s of %s' % (levelNum + 1, len(levels)), 1, TEXTCOLOR)
    levelRect = levelSurf.get_rect()
    levelRect.bottomleft = (20, WINHEIGHT - 35)
    mapWidth = len(mapObj) * TILEWIDTH
    mapHeight = (len(mapObj[0]) - 1) * TILEFLOORHEIGHT + TILEHEIGHT
    MAX_CAM_X_PAN = abs(HALF_WINHEIGHT - int(mapHeight / 2)) + TILEWIDTH
    MAX_CAM_Y_PAN = abs(HALF_WINWIDTH - int(mapWidth / 2)) + TILEHEIGHT

    levelIsComplete = False
    # Track how much the camera has moved:
    cameraOffsetX = 0
    cameraOffsetY = 0
    # Track if the keys to move the camera are being held down:
    cameraUp = False
    cameraDown = False
    cameraLeft = False
    cameraRight = False

    print("runlevel variables set")

    loop = 0

    while True: # Main loop

        loop += 1

        if loop == 1:
            print("loop started")


        #Reset these variables:
        playerMoveTo = None
        keyPressed = False

        for event in pygame.event.get(): # Event handling loop
            if event.type == QUIT:
                # Player clicked X at the corners
                terminate()

            elif event.type == KEYDOWN:
                print("Key Pressed")
                # Handle key presses
                keyPressed = True
                if event.key == K_LEFT:
                    playerMoveTo = LEFT
                elif event.key == K_RIGHT:
                    playerMoveTo = RIGHT
                elif event.key == K_UP:
                    playerMoveTo = UP
                elif event.key == K_DOWN:
                    playerMoveTo = DOWN

                # Set the camera to move mode
                elif event.key == K_a:
                    cameraLeft = True
                elif event.key == K_d:
                    cameraRight = True
                elif event.key == K_s:
                    cameraDown = True
                elif event.key == K_w:
                    cameraUp = True

                elif event.key == K_n:
                    return 'next'
                elif event.key == K_b:
                    return 'back'

                elif event.key == K_ESCAPE:
                    terminate()
                elif event.key == K_BACKSPACE:
                    return 'reset'
                elif event.key == K_p:
                    #Change the player image to the next one
                    currentImage += 1
                    if currentImage >= len(PLAYERIMAGES):
                        #After the last player image, use the first one
                        currentImage = 0
                    mapNeedsRedraw = True
            elif event.type == KEYUP:
                #Unset the camera move mode
                if event.key == K_a:
                    cameraLeft = False
                elif event.key == K_d:
                    cameraUp = False
                elif event.key == K_s:
                    cameraDown = False
                elif event.key == K_d:
                    cameraRight = False

        if playerMoveTo != None and not levelIsComplete:
            #If the player pushed a key to move, make the move, if possible, push stars that are pushable
            moved = makeMove(mapObj, gameStateObj, playerMoveTo)

            if moved:
                #Increment step counter
                gameStateObj['stepCounter'] += 1
                mapNeedsRedraw = True

            if isLevelFinished(levelObj, gameStateObj):
                #Level is complete, show solved
                levelIsComplete = True
                keyPressed = False

        DISPLAYSURF.fill(BGCOLOR)

        if mapNeedsRedraw:
            mapSurf = drawMap(mapObj, gameStateObj, levelObj['goals'])
            mapNeedsRedraw = False

        if cameraUp and cameraOffsetY < MAX_CAM_X_PAN:
            cameraOffsetY += CAM_MOVE_SPEED
        elif cameraDown and cameraOffsetY > -MAX_CAM_X_PAN:
            cameraOffsetY -= CAM_MOVE_SPEED
        if cameraLeft and cameraOffsetX < MAX_CAM_Y_PAN:
            cameraOffsetX += CAM_MOVE_SPEED
        elif cameraRight and cameraOffsetX > -MAX_CAM_Y_PAN:
            cameraOffsetX -= CAM_MOVE_SPEED

        #Adjust mapSurf's rect object based on the camera offsets
        mapSurfRect = mapSurf.get_rect()
        mapSurfRect.center = (HALF_WINWIDTH + cameraOffsetX, HALF_WINHEIGHT + cameraOffsetY)

        # Draw mapSurf to the DISPLAYSURF surfaceobject
        DISPLAYSURF.blit(mapSurf, mapSurfRect)

        DISPLAYSURF.blit(levelSurf, levelRect)
        stepSurf = BASICFONT.render('Steps: %s' %(gameStateObj['stepCounter']), 1, TEXTCOLOR)
        stepRect = stepSurf.get_rect()
        stepRect.bottomleft = (20, WINHEIGHT - 10)
        DISPLAYSURF.blit(stepSurf, stepRect)

        if levelIsComplete:
            # is solved, show the 'solved' image until the player has pressed a key
            solvedRect = IMAGESDICT['solved'].get_rect()
            solvedRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)
            DISPLAYSURF.blit(IMAGESDICT['solved'], solvedRect)

            if keyPressed:
                return 'solved'

        pygame.display.update()
        FPSCLOCK.tick()

def isWall(mapObj, x, y):
    """Returns True if the (x, y) position on
    the map is a wall, otherwise return False."""
    if x < 0 or x >= len(mapObj) or y < 0 or y >= len(mapObj[x]):
        return False # x and y aren't actually on the map.
    elif mapObj[x][y] in ('#', 'x'):
        return True # wall is blocking
    return False



def decorateMap(mapObj, startxy):
    # Makes a copy of the given map object and modifies it:
    # walls that are corners are turned into corners
    # Outside floor/inside floors are made separate
    # Trees and rocks are added to the outside tiles.

    #Returns the decorated map object

    startx,starty = startxy # Syntactic sugar

    #Copy th map object so we don't modify the original passed
    mapObjCopy = copy.deepcopy(mapObj)

    # Remove the non-wall characters
    for x in range(len(mapObjCopy)):
        for y in range(len(mapObjCopy[0])):
            if mapObjCopy[x][y] in ('$','.','@','+','*'):
                mapObjCopy[x][y] = ''

    #Flood fill to determine inside/outside floor tiles
    floodFill(mapObjCopy,startx,starty,'','o')

    #Convert the adjoined walls into corner tiles
    for x in range(len(mapObjCopy)):
        for y in range(len(mapObjCopy[0])):

            if mapObjCopy[x][y] == '#':
                if (isWall(mapObjCopy, x, y-1) and isWall(mapObjCopy, x+1, y)) or \
                   (isWall(mapObjCopy, x+1, y) and isWall(mapObjCopy, x, y+1)) or \
                   (isWall(mapObjCopy, x, y+1) and isWall(mapObjCopy, x-1, y)) or \
                   (isWall(mapObjCopy, x-1, y) and isWall(mapObjCopy, x, y-1)):
                    mapObjCopy[x][y] = 'x'

            elif mapObjCopy[x][y] == '' and random.randint(0,99) < OUTSIDE_DECORATION_PCT:
                mapObjCopy[x][y] = random.choice(list(OUTSIDEDECOMAPPING.keys()))

    return mapObjCopy

def isBlocked(mapObj,gameStateObj,x,y):
    # Returns true if the x,y position is blocked by a wall or a star. Else return false

    if isWall(mapObj,x,y):
        return True

    elif x < 0 or x >= len(mapObj) or y < 0 or y >= len(mapObj[x]):
        return True # x,y is outside the map

    elif (x,y) in gameStateObj['stars']:
        return True # Star is blocking

    return False

def makeMove(mapObj,gameStateObj,playerMoveTo):
    # Given a map,state we can see if it is possible for player to make current move. If it is, we change
    # player position (and star if it's being pushed)-

    # Returns true if player moved, otherwise False

    # Make sure the player can move in the direction they want
    playerx, playery = gameStateObj['player']

    # This variable is "Syntactic sugar". Typing stars is more readable than gameStateObj['stars']
    stars = gameStateObj['stars']

    # The code for handling each directions is similar aside from adding 1 to x,y coorindates we can simplify with offsets
    if playerMoveTo == UP:
        xOffset = 0
        yOffset = -1
    elif playerMoveTo == RIGHT:
        xOffset = 1
        yOffset = 0
    elif playerMoveTo == LEFT:
        xOffset = -1
        yOffset = 0
    elif playerMoveTo == DOWN:
        xOffset = 0
        yOffset = 1

    # See if the player can move in that direction
    if isWall(mapObj,playerx + xOffset,playery + yOffset):
        return False
    else:
        if (playerx + xOffset, playery + yOffset) in stars:
            # Movethestar
            if not isBlocked(mapObj,gameStateObj,playerx + (xOffset*2),playery + (yOffset*2)):
                # Move the star
                ind = stars.index((playerx + xOffset,playery + yOffset))
                stars[ind] = (stars[ind][0] + xOffset, stars[ind][1] + yOffset)
            else:
                return False
        # Move the player upwards
        gameStateObj['player'] = (playerx + xOffset,playery + yOffset)
        return True

def startScreen():
    # Display start screen until key is pressed

    # Position title image
    titleRect = IMAGESDICT['title'].get_rect()
    topCoord = 50 # topCoord tracks where to posiiton the top of the TEXTCOLOR
    titleRect.top = topCoord
    titleRect.centerx = HALF_WINWIDTH
    topCoord += titleRect.height

    #Unfortunately, pygame font system shows one line at a time, we can tuse /n so we use a list
    instructionText = ['Push the stars over the marks.',
    'Arrow keys to move, WASD for camera control, P to change character',
    'Backspace to reset level, Esc to quit',
    'N for next level']

    #Start with drawing a black color to the entire window
    DISPLAYSURF.fill(BGCOLOR)

    #Draw the title image to the window
    DISPLAYSURF.blit(IMAGESDICT['title'],titleRect)

    #Position and draw the text
    for i in range(len(instructionText)):
        instSurf = BASICFONT.render(instructionText[i], 1, TEXTCOLOR)
        instRect = instSurf.get_rect()
        topCoord += 10 # 10 pixels between each line of text
        instRect.top = topCoord
        instRect.centerx = HALF_WINWIDTH
        topCoord += instRect.height # Adjust for the height of the line
        DISPLAYSURF.blit(instSurf, instRect)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return # User has pressed a key, so return

        # Display the Displaysurf contents to the actual
        pygame.display.update()
        FPSCLOCK.tick()

def readLevelsFile(filename):
    assert os.path.exists(filename), 'Cannot find the level file: %s' %(filename)
    mapFile = open(filename, 'r')
    #Each level must end with a blank line
    content = mapFile.readlines() + ['\r\n']
    mapFile.close()

    levels = [] # Will contain a list of level objects
    levelNum = 0
    mapTextLines = [] # Contains the list for a single level's map
    mapObj = [] # the map object made from the data in mapTextLines
    for lineNum in range(len(content)):
        # Process each line that was in the level file
        line = content[lineNum].rstrip('\r\n')

        if ';' in line:
            # Ignore the ; lines, theyre comments in the level file
            line = line[:line.find(';')]

        if line != '':
            #This line is a part of the map
            mapTextLines.append(line)
        elif line == '' and len(mapTextLines) > 0:
            # A blank line indicates the end of a level's map in the file.
            # Convert the text in mapTextLines into a level object.

            #Find the longest row in the map
            maxWidth = -1
            for i in range(len(mapTextLines)):
                if len(mapTextLines[i]) > maxWidth:
                    maxWidth = len(mapTextLines[i])
            # Add spaces to the ends of the shorter rows. This ensures the map will be rectangular
            for i in range(len(mapTextLines)):
                mapTextLines[i] += ' ' * (maxWidth - len(mapTextLines[i]))

            for x in range(len(mapTextLines[0])):
                mapObj.append([])
            for y in range(len(mapTextLines)):
                for x in range(maxWidth):
                    mapObj[x].append(mapTextLines[y][x])

            #Loop through the spaces in the map and find the @, ., and $ characters before starting game state
            startx = None
            starty = None
            goals = [] # List of (x,y) tuples for each goals
            stars = [] # List of (x,y) tuples for each star starting position
            for x in range(maxWidth):
                for y in range(len(mapObj[x])):
                    if mapObj[x][y] in ('@','+'):
                        # '@' is a player, + is player and goal
                        startx = x
                        starty = y
                    if mapObj[x][y] in ('.','+','*'):
                        # . is a goal, * is start and goal
                        goals.append((x,y))
                    if mapObj[x][y] in ('$','*'):
                        # $ is star
                        stars.append((x,y))

            # Basic level design sanity checks:
            assert startx != None and starty != None, 'Level %s (around line %s) in %s is missing a "@" or "+" to mark the start point' % (levelNum+1, lineNum, filename)
            assert len(goals) > 0, 'Level %s (around line %s) in %s must have at least one goal.' %(levelNum+1, lineNum, filename)
            assert len(stars) >= len(goals), 'Level %s (around line %s) in %s is impossible to solve.It has %s goals but only %s stars.' %(levelNum+1, lineNum, filename, len(goals), len(stars))

            #Create level object and starting game state object.
            gameStateObj = {'player': (startx, starty),
                            'stepCounter' : 0,
                            'stars' : stars}
            levelObj = {'width' : maxWidth,
                        'height' : len(mapObj),
                        'mapObj' : mapObj,
                        'goals' : goals,
                        'startState' : gameStateObj}

            levels.append(levelObj)

            # Reset the variables for reading the next map.
            mapTextLines = []
            mapObj = []
            gameStateObj = {}
            levelNum += 1

    return levels

def floodFill(mapObj, x, y, oldCharacter, newCharacter):
    # Changes any values matching old characters on the map object to newCharacter at the (x,y) position, and does the same for the positions left, right, down, and up of (x,y) recursively.

    # Flood fill creates inside/outside floor distinction with recursive functions.

    if mapObj[x][y] == oldCharacter:
        mapObj[x][y] = newCharacter

    if x < len(mapObj) - 1 and mapObj[x+1][y] == oldCharacter:
        floodFill(mapObj, x+1, y, oldCharacter, newCharacter) # Call right
    if x > 0 and mapObj[x-1][y] == oldCharacter:
        floodFill(mapObj, x-1, y, oldCharacter, newCharacter) # Call left
    if y < len(mapObj[x]) - 1 and mapObj[x][y+1] == oldCharacter:
        floodFill(mapObj, x, y+1, oldCharacter, newCharacter) # Call Down
    if y > 0 and mapObj[x][y-1] == oldCharacter:
        floodFill(mapObj, x, y-1, oldCharacter, newCharacter) # Call up

def drawMap(mapObj, gameStateObj, goals):
    # Draws the map to a surface object, including the player and stars. This function does not call pygame.display.update(), nor does it draw the 'level' and 'steps' text in the corner.
    # Map surf will be the single surface object that the tiles are drawn on, so that it is easy to position the entire map on the displaysurf surface object. First, the width and height must be calculated.
    mapSurfWidth = len(mapObj) * TILEWIDTH
    mapSurfHeight = (len(mapObj[0]) - 1)* TILEFLOORHEIGHT + TILEHEIGHT
    mapSurf = pygame.Surface((mapSurfWidth, mapSurfHeight))
    mapSurf.fill(BGCOLOR) # Start with a blank color on the surface

    #Draw the tile sprites onto this surface
    for x in range(len(mapObj)):
        for y in range(len(mapObj[x])):
            spaceRect = pygame.Rect((x * TILEWIDTH, y * TILEFLOORHEIGHT, TILEWIDTH, TILEHEIGHT))
            if mapObj[x][y] in TILEMAPPING:
                baseTile = TILEMAPPING[mapObj[x][y]]
            elif mapObj[x][y] in OUTSIDEDECOMAPPING:
                baseTile = TILEMAPPING[' ']

            # First draw the base ground/wall tile.
            mapSurf.blit(baseTile, spaceRect)

            if mapObj[x][y] in OUTSIDEDECOMAPPING:
                #Draw any tree/rock decorations that are on this tile.
                mapSurf.blit(OUTSIDEDECOMAPPING[mapObj[x][y]], spaceRect)
            elif (x,y) in gameStateObj['stars']:
                if (x,y) in goals:
                    # A goal AND star are on this space, draw goal first.
                    mapSurf.blit(IMAGESDICT['covered goal'], spaceRect)
                #Then draw the star sprites
                mapSurf.blit(IMAGESDICT['star'], spaceRect)
            elif (x,y) in goals:
                #Draw the goal without a star on it.
                mapSurf.blit(IMAGESDICT['uncovered goal'],spaceRect)

            #Last draw the player on the board:
            if (x,y) == gameStateObj['player']:
                #Note: the value 'currentImages' refers
                #To a key in playerimages which has the specific player image we want to shows
                mapSurf.blit(PLAYERIMAGES[currentImage], spaceRect)

    return mapSurf

def isLevelFinished(levelObj, gameStateObj):
    # Returns true if all goals have stars in them
    for goal in levelObj['goals']:
        if goal not in gameStateObj['stars']:
            # Found a space with a goal but no star in it
            return False
    return True

def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
