import random
import pygame
from pygame.locals import *

from gamelib.palette import *
from gamelib.gamemodels import *
CHEAT = True

def DrawForeground(Surface, State, ScreenSize):
    
    fgRect = Rect(0,int(ScreenSize[1]/2),ScreenSize[0],int(ScreenSize[1]/2))
    
    SectorDetails = State.GetSectorsAhead()
    print(SectorDetails)
    
    #Back Sector
    if not SectorDetails[2] is None:
        bsr = Rect(0, fgRect.h, fgRect.w, int(fgRect.h/4))
        DrawGradient(Surface, GetGroundColour(SectorDetails[2],State.DayPhase), bsr)
        if "tree" in SectorDetails[2]:
            DrawTree(Surface, SectorDetails[2]["tree"], bsr, 0.25)
            
    #Mid Sector
    if not SectorDetails[1] is None:
        msr = Rect(0, fgRect.h+int(fgRect.h/4), fgRect.w, int(fgRect.h/4))
        DrawGradient(Surface, GetGroundColour(SectorDetails[1],State.DayPhase), msr)
        if "tree" in SectorDetails[1]:
            DrawTree(Surface, SectorDetails[1]["tree"], msr, 0.5)
            
    #Front Sector
    fsr = Rect(0, fgRect.h+int(fgRect.h/2), fgRect.w, int(fgRect.h/2))
    DrawGradient(Surface, GetGroundColour(SectorDetails[0],State.DayPhase), fsr)

    if "tree" in SectorDetails[0]:
        DrawTree(Surface, SectorDetails[0]["tree"], fsr)
    if "shore" in SectorDetails[0]:
        DrawReeds(Surface, SectorDetails[0]["shore"], fsr)

def DrawForeground2(Surface, State, ScreenSize):
    
    fgRect = Rect(0,int(ScreenSize[1]/2),ScreenSize[0],int(ScreenSize[1]/2))
    bsr = Rect(0, fgRect.h, fgRect.w, int(fgRect.h/4))
    msr = Rect(0, fgRect.h+int(fgRect.h/4), fgRect.w, int(fgRect.h/4))
    fsr = Rect(0, fgRect.h+int(fgRect.h/2), fgRect.w, int(fgRect.h/2))
    SectorDetails = State.GetSectorsAhead()
    
    if not SectorDetails[2] is None:
        DrawSector(Surface, State, SectorDetails[2], bsr, 0.18)
    if not SectorDetails[1] is None:
        DrawSector(Surface, State, SectorDetails[1], msr, 0.5)
    if not SectorDetails[0] is None:
        DrawSector(Surface, State, SectorDetails[0], fsr, 1)
        
def DrawSector(Surface, State, SectorDetails, sr, Scale):
    DrawGradient(Surface, GetGroundColour(SectorDetails,State.DayPhase), sr)

    if "tree" in SectorDetails:
        DrawTree(Surface, SectorDetails["tree"], sr, Scale)
    if "shore" in SectorDetails:
        DrawReeds(Surface, SectorDetails["shore"], sr, Scale)
    if "mushroom" in SectorDetails:
        DrawMushroom(Surface, SectorDetails["mushroom"], sr, Scale)
    if "flowers" in SectorDetails:
        DrawFlower(Surface, SectorDetails["flowers"], sr, Scale)

def GetGroundColour(SectorDetails, DayPhase):
    
    g = Color(255, 155, 155)
    if "water" in SectorDetails:
        g = Water[DayPhase]
    elif "shore" in SectorDetails:
        g = Shore[DayPhase]
    elif "snow" in SectorDetails:
        g = Snow[DayPhase]
    elif "tree" in SectorDetails:
        g = WoodGround[DayPhase]
    elif "ground" in SectorDetails:
        g = Ground[DayPhase]
    return g
    
def DrawReeds(Surface, PosList, DispRect, Scale = 1):
    for reedPos in PosList:
        t = MakeReeds()
        DrawObject(Surface, t, DispRect, Scale, reedPos)

def DrawFlower(Surface, Pos, DispRect, Scale = 1):
    t = MakeFlowers()
    DrawObject(Surface, t, DispRect, Scale, Pos)
    print("Draw Flower")
    
def DrawMushroom(Surface, Pos, DispRect, Scale = 1):
    t = MakeMushroom()
    DrawObject(Surface, t, DispRect, Scale, Pos)
    
def DrawTree(Surface, Pos, DispRect, Scale = 1):
    t = MakeTree()
    DrawObject(Surface, t, DispRect, Scale, Pos)
    
def DrawObject(Surface, t, DispRect, Scale, Pos):
    t.Width = int(t.Width*Scale)
    t.Height = int(t.Height*Scale)
    t.Pos = [DispRect.x + int((Pos[0]/100)*DispRect.w), DispRect.y + int((Pos[1]/100)*DispRect.h)]
    t.Pos[1] -= t.Size()[1]
    if t.Pos[0] + t.Size()[0]> DispRect.w:
        t.Pos[0] = DispRect.w - t.Size()[0]
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
                if "flowers" in r:
                    c = Color(0, 0, 0)
            
            pygame.draw.rect(surface, c, Rect(x*tile, y*tile, tile, tile ), 0) 

    pr = Rect(tile*moonmap.PlayerPos[0], tile*moonmap.PlayerPos[1], tile, tile)
    pygame.draw.rect(surface,Color(255,0,0),pr)
