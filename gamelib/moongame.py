import sys
import pygame
from pygame.locals import *

from gamelib.moonstate import *
from gamelib.util import *
from gamelib.gfx import *
from gamelib.palette import *

CHEAT = True

class MoonGame(object):
    """
        Moon game class.
    """
    def __init__(self, Surface, Screen, ScreenSize):
        self.Screen = Screen
        self.Surface = Surface
        self.ScreenSize = ScreenSize
        self.State = MoonState()
        self.MapOnView = False
    
    def MainLoop(self):
        
        self.DrawSector()

        while True:#self.P1.Health >0 and not self.Victory:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    keystate = pygame.key.get_pressed()
                    if keystate[K_ESCAPE]==1:
                        return
                    if keystate[K_m]==1:
                        self.MapOnView = not self.MapOnView
                elif event.type == ANIMEVENT:
                    if self.MapOnView == False:
                        self.DrawSector()
                    else:
                        self.Surface.fill(pygame.Color("black"))
                        DrawMap(self.Surface, self.State)
                        self.UpdateScreen()

    def UpdateScreen(self):
        self.Screen.blit(self.Surface, (0, 0))
        pygame.display.flip()
        
    def DrawSector(self):
        if CHEAT:
            print("Sector")
            print(str(self.State.CurrSector()))
        self.Surface.fill(pygame.Color("black"))
        
        DrawGradient(self.Surface, Sky[self.State.DayPhase], Rect(0,0,640,240))
        DrawText(self.Surface, 10, 50, "You are on the Moon...", 14, (255,0,0) )
        DrawForeground(self.Surface, self.State, self.ScreenSize)
        self.UpdateScreen()
        
