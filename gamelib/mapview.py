import pygame
import sys
from pygame.locals import *
from moonmodel import *

if __name__=="__main__":
    WINSIZE = 640,680
    pygame.init()
    screen = pygame.display.set_mode(WINSIZE,0,8)
    pygame.display.set_caption("Map Viewer")
    pygame.init()
    
    def drawMoon(screen):
        o = MoonModel(256)
        o.Generate()
        tile = 2
        w = o.Width
        for x in range(w):
            for y in range(w):
                r = o.Sectors[x][y]
                c = Color(255,255,255)
                if "water" in r:
                    c = Color(0, 0, 255)
                elif "tree" in r:
                    c = Color(128, 255, 0)
                elif "ground" in r:
                    c = Color(0, 255, 0)
                
                pygame.draw.rect(screen, c, Rect(x*tile, y*tile, tile, tile ), 0) 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                keystate = pygame.key.get_pressed()
                if keystate[K_a]==1:
                    drawMoon(screen)
                if keystate[K_ESCAPE]==1:
                    sys.exit()
        pygame.display.update()
