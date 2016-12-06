def heuristics(playerx,playery,aix,aiy):
    xdistance = abs(playerx-aix)
    ydistance = abs(playery-aiy)

    if xdistance < ydistance: #Ai is further in Y direction
        if playery > aiy:
            return "DOWN"
        else:
            return "UP"
    elif xdistance > ydistance:
        if playerx > aix: #Ai is futher in X direction
            return "RIGHT"
        else:
            return "LEFT"
    elif xdistance == ydistance: #Same distance
    
        randomNumber = random.randint(0, 3)
        if randomNumber == 0:
            return "RIGHT"
        elif randomNumber == 1:
            return "LEFT"
        elif randomNumber == 2:
            return "UP"
        elif randomNumber == 3:
            return "DOWN"
