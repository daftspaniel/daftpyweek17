import random
import pygame
from pygame.locals import *

class ObjectView(object):

    """
    Draw graphics on 8x8 grid scaled as required.
    """

    def __init__(self, Data, Colours, Pos, ForeColours = None):

        self.Data = Data
        self.Colours = Colours
        self.ForeColours = ForeColours
        self.Width = 20
        self.Height = 40
        self.Pos = Pos
    def Size(self):
        return (self.Width*8, self.Height*8)
    def Draw(self, surface):
        for x in range(0,8):
            for y in range(0,8):
                
                c = self.Data[y][x]
                if c=="1": 
                    p = self.Colours[y]
                    pygame.draw.rect(surface, p, Rect(self.Pos[0] + x*self.Width, self.Pos[1] + y*self.Height, self.Width, self.Height) , 0)
                elif not c=="0": 
                    p = self.ForeColours[int(c)-2]
                    pygame.draw.rect(surface, p, Rect(self.Pos[0] + x*self.Width, self.Pos[1] + y*self.Height, self.Width, self.Height) , 0)

def MakeTree():
    t = ["","","","","","","",""]
    cols = [Color(0,255,0),Color(0,239,0),Color(70,223,0),Color(125,242,13),Color(94,20,0),Color(78,20,0),Color(62,20,0),Color(46,20,0)]

    t[0] = "01111110"
    t[1] = "11111111"
    t[2] = "11111111"
    t[3] = "01111110"
    t[4] = "00011000"
    t[5] = "00011000"
    t[6] = "00011000"
    t[7] = "00011000"
    
    return ObjectView(t,cols, (50,140))
    
def MakeBush():
    t = ["","","","","","","",""]
    cols = []
    g = Color(0,192,192)
    
    for i in range(6):
        d = (16*i)
        cols.append(Color(0, g.g - d, 0))
    cols.append(Color(92,50,0))
    cols.append(Color(76,50,0))
    t[0] = "01111110"
    t[1] = "11111111"
    t[2] = "11111111"
    t[3] = "11111111"
    t[4] = "11111111"
    t[5] = "11111111"
    t[6] = "00111100"
    t[7] = "00111100"
    
    o = ObjectView(t,cols, (420,250))
    o.Width = 5
    o.Height = 5
    return o
    
def MakeMushroom():
    t = ["","","","","","","",""]
    cols = []
    fcols = [Color(255, 0, 0)]
    g = Color(192,192,192)
    
    for i in range(8):
        d = (16*i)
        cols.append(Color( g.g - d, g.g - d,  g.g - d))

    t[0] = "01111110"
    t[1] = "11111111"
    t[2] = "12121211"
    t[3] = "11111111"
    t[4] = "11212121"
    t[5] = "11111111"
    t[6] = "00111100"
    t[7] = "00111100"
    
    o = ObjectView(t,cols, (32,310), fcols)
    o.Width = 10
    o.Height = 10
    return o

def MakeReeds():
    t = ["","","","","","","",""]
    cols = [Color(0,255,0),Color(0,239,0),Color(0,223,0),Color(0,207,0),Color(94,20,0),Color(78,20,0),Color(62,20,0),Color(46,20,0)]
    cols.reverse()
    t[0] = "00000000"
    t[1] = "00000000"
    t[2] = "01000000"
    t[3] = "01000000"
    t[4] = "01000100"
    t[5] = "01000101"
    t[6] = "11010101"
    t[7] = "11010101"
    
    o = ObjectView(t,cols, (580,200))
    o.Width = 5
    o.Height = 20
    return o

def MakeFlowers():
    t = ["","","","","","","",""]
    cols = [Color(0,255,0),Color(0,239,0),Color(0,223,0),Color(0,207,0),Color(194,2,0),Color(178,2,0),Color(162,2,0),Color(146,2,0)]
    cols.reverse()
    t[0] = "00000000"
    t[1] = "00100000"
    t[2] = "01110000"
    t[3] = "00100000"
    t[4] = "00100100"
    t[5] = "00101110"
    t[6] = "01110101"
    t[7] = "11110101"
    o = ObjectView(t,cols, (400,280))
    o.Width = 3
    o.Height = 8
    return o
    
def MakeRock():
    t = ["","","","","","","",""]
    cols = []
    g = Color(192,192,192)
    g = Color(164,128,28)
    for i in range(8):
        d = (16*i)
        #cols.append(Color(g.r - d, g.g - d, g.b - d))
        cols.append(Color(g.r - d, g.g - d, g.b))
    
    t[0] = "01111110"
    t[1] = "11111111"
    t[2] = "11111111"
    t[3] = "11111111"
    t[4] = "11111111"
    t[5] = "11111111"
    t[6] = "11111111"
    t[7] = "01111110"
    o = ObjectView(t,cols, (200,290))
    o.Width = 7
    o.Height = 7
    return o
    
def MakeYellowBug():
    t = ["","","","","","","",""]
    cols = []
    fcols = [Color(255, 242, 0), Color(255, 0, 0), Color(63,73,204), Color(0,162,232) ]
    g = Color(148,148,148)
    for i in range(8):
        d = (16*i)
        cols.append(Color(g.r - d, g.g - d, g.b - d))
    
    t[0] = "00111100"
    t[1] = "01222210"
    t[2] = "12322321"
    t[3] = "12322321"
    t[4] = "12244221"
    t[5] = "12222221"
    t[6] = "11111111"
    t[7] = "05500550"
    o = ObjectView(t,cols, (250,290), fcols)
    o.Width = 15
    o.Height = 15
    return o

def MakeMountains():
    t = ["","","","","","","",""]
    cols = []
    g = Color(255, 255, 255)
    for i in range(8):
        d = (16*i)
        cols.append(Color(g.r - d, g.g - d, g.b - d))
    
    t[0] = "00100000"
    t[1] = "01110000"
    t[2] = "01110110"
    t[3] = "11111111"
    t[4] = "11111111"
    t[5] = "11111111"
    t[6] = "11111111"
    t[7] = "11111111"
    o = ObjectView(t,cols, (0,160))
    o.Width = 60
    o.Height = 15
    return o
