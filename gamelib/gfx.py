import random
import pygame
from pygame.locals import *

from gamelib.palette import *

CHEAT = True

def DrawForeground(Surface, State, ScreenSize):
    DrawGradient(Surface, Ground[State.DayPhase], Rect(0,int(ScreenSize[1]/2),ScreenSize[0],int(ScreenSize[1]/2)))
    DrawTree(Surface)
    
def DrawTree(Surface):
    t = MakeTree()
    t.Draw(Surface)
    
def DrawGradient(Surface, SkyColor, SkyR):
    src = Rect(SkyR.x,SkyR.y, SkyR.w, int(SkyR.h/10) )
    csky = SkyColor
    for i in range(10):
       src = Rect(SkyR.x, SkyR.y + (src.h*i), SkyR.w, src.h  )
       bbb = csky.b-(i*8)
       if bbb<0:bbb=0
       pygame.draw.rect(Surface, Color(csky.r,csky.g,bbb), src, 0)

def DrawMap(surface, moonmap):
    
    tile = 4
    w = moonmap.Model.Width
    S = moonmap.Model.Sectors
    
    for x in range(w):
        for y in range(w):
            r = S[x][y]
            if CHEAT or "visited" in r:
                c = Color(255,255,255)
                if "water" in r:
                    c = Color(0, 0, 255)
                elif "shore" in r:
                    c = Color(128, 64, 0)
                elif "tree" in r:
                    c = Color(128, 255, 0)
                elif "snow" in r:
                    c = Color(255, 255, 255)
                elif "ground" in r:
                    c = Color(0, 255, 0)
            
            pygame.draw.rect(surface, c, Rect(x*tile, y*tile, tile, tile ), 0) 

    pr = Rect(tile*moonmap.PlayerPos[0], tile*moonmap.PlayerPos[1], tile, tile)
    pygame.draw.rect(surface,Color(255,0,0),pr)

class ObjectView(object):

    """
    Class Description
    """

    def __init__(self, Data, Colours, Pos):

        self.Data = Data
        self.Colours = Colours
        self.Width = 10
        self.Height = 20
        self.Pos = Pos
        
    def Draw(self, surface):
        for x in range(0,8):
            for y in range(0,8):
                
                c = self.Data[y][x]
                if c=="1": 
                    p = self.Colours[y]
                    pygame.draw.rect(surface, p, Rect(self.Pos[0] + x*self.Width, self.Pos[1] + y*self.Height, self.Width, self.Height) , 0)
                    

def MakeTree():
    t = ["","","","","","","",""]
    cols = [Color(0,255,0),Color(0,239,0),Color(0,223,0),Color(0,207,0),Color(94,20,0),Color(78,20,0),Color(62,20,0),Color(46,20,0)]

    t[0] = "01111110"
    t[1] = "11111111"
    t[2] = "11111111"
    t[3] = "01111110"
    t[4] = "00011000"
    t[5] = "00011000"
    t[6] = "00011000"
    t[7] = "00011000"
    
    return ObjectView(t,cols, (50,140))
