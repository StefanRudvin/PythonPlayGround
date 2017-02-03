# Travelling salesman algorithm
import math, os

pointstovisit = [(2,0),(0,3),(3,3),(1,2),(1,1),(4,5),(7,5),(6,5),(8,9),(7,7),(1,6),(7,1),(9,1)]

def main():
    mapheight = 9
    mapwidth = 9
    print("-----Traveling salesman algorithm.-----")
    print("Points to visit:", pointstovisit)
    print("Map size is:", mapheight, "by", mapwidth)

    visitednodes = [(0,0)]
    input()
    while len(pointstovisit) > 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Nodes left:",len(pointstovisit))
        print("Node:",visitednodes[-1])
        mapObject = buildmap(mapheight,mapwidth,pointstovisit, visitednodes)

        printmap(mapObject)
        userinput = input()
        visitednodes.append(move(pointstovisit,visitednodes[-1]))

    print("All nodes found!")

def move(pointstovisit,startpoint):
    nextnode = findnextmove(pointstovisit,startpoint)

    pointstovisit.remove(nextnode)

    return nextnode

def printmap(mymap):
    for array in mymap:
        print(array)

def buildmap(height,width,endpoints,visitednodes):
    x = 0
    result = []
    marked = False
    markedvisited = False
    while x < height:
        xarray = []
        y = 0
        while y < width:
            for visitedx,visitedy in visitednodes:
                if visitedx == x and visitedy == y:
                    xarray.append(("O"))
                    visited = True

            if not visited:
                for pointx,pointy in endpoints:
                    if x == pointx and y == pointy:
                        xarray.append(("X"))
                        marked = True
                if not marked and not visited:
                    xarray.append(("."))
                else:
                    marked = False
            else:
                visited = False
            y+= 1
        x += 1
        result.append(xarray)
    return result

def findnextmove(locations,start):
    startpoint = start
    mindistance = math.inf
    nextmove = ()

    for point in locations:
        distance = heuristics(*startpoint,*point)
        if distance < mindistance:
            mindistance = distance
            nextmove = point
    return nextmove

def heuristics(x1,y1,x2,y2):
    distance = 0
    if x1 == x2:
        if y2 == y1:
            distance = 0
        else:
            distance = abs(y2-y1)
    else:
        if y2 == y1:
            distance = abs(x2-x1)
        else:
            distance = math.sqrt((abs(x2-x1))**2 + (abs(y2-y1))**2)
    return distance

main()
