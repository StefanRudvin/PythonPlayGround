import random, sys, os, pygame, ghostai, readfile, pathfind
from pathfind import *

def initialize():
    ghostai.initialize()
    readfile.initialize()

def terminate():
    pygame.quit()
    sys.exit()

def showStartScreen(DISPLAYSURF,BASICFONT,FPSCLOCK,BGCOLOR):
    titleFont = pygame.font.Font('freesansbold.ttf',100)
    titleSurf = titleFont.render('Pathfinder',True,WHITE,DARKGREEN)

    while True:
        DISPLAYSURF.fill(BGCOLOR)
        titleRect = titleSurf.get_rect()
        titleRect.center = (WINWIDTH/2,WINHEIGHT/2)
        DISPLAYSURF.blit(titleSurf,titleRect)


        makerSurf = BASICFONT.render('Code from inventwithpython.com, Modified by Stefan Rudvin', True, WHITE)
        makerRect = makerSurf.get_rect()
        makerRect.topleft = (30,WINHEIGHT -20)
        DISPLAYSURF.blit(makerSurf,makerRect)

        drawText("topLeft",DISPLAYSURF,BASICFONT,BGCOLOR,"topLeft",20)
        drawText("topRight",DISPLAYSURF,BASICFONT,BGCOLOR,"topRight",20)
        drawText("bottomleft",DISPLAYSURF,BASICFONT,BGCOLOR,"bottomLeft",20)
        drawText("bottomRight",DISPLAYSURF,BASICFONT,BGCOLOR,"bottomRight",20)

        drawText("Press any key to play", DISPLAYSURF,BASICFONT,BGCOLOR,"topLeft",300)
        #Make function for keypress HERE

        if checkforKeyPress():
            pygame.event.get()
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)


#Combine Surf and rect funcs
def drawText(String,DISPLAYSURF,BASICFONT,BGCOLOR,position,padding):
    surf = drawSurf(String, DISPLAYSURF,BASICFONT,BGCOLOR)
    rect = drawRect(surf)
    rectPosition(position,padding,rect)
    return DISPLAYSURF.blit(surf,rect)

#Function to return Surf
def drawSurf(string,DISPLAYSURF,BASICFONT,BGCOLOR):
    StringSurf = BASICFONT.render(string, True, WHITE)
    return StringSurf

#Func to return Rect
def drawRect(StringSurf):
    StringRect = StringSurf.get_rect()
    return StringRect

def rectPosition(position,padding,rect):
    if position == "topLeft":
        rect.topleft = (padding,padding)
        return rect.topleft
    elif position == "topRight":
        rect.topleft = (WINWIDTH - padding * 5,padding)
        return rect.topleft
    elif position == "bottomRight":
        rect.topleft = (WINWIDTH - padding * 5,WINHEIGHT - padding * 2)
        return rect.topleft
    elif position == "bottomLeft":
        rect.bottomleft = (padding,WINHEIGHT - padding * 2)
        return rect.topleft
    else:
        raise Exception("Position not set!")

def checkforKeyPress():
    if len(pygame.event.get(QUIT))>0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key
