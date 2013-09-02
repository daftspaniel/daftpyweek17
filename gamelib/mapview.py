import pygame
import sys
from pygame.locals import *
from moonmodel import *

o = None

if __name__=="__main__":
    WINSIZE = 640,680
    pygame.init()
    screen = pygame.display.set_mode(WINSIZE,0,8)
    pygame.display.set_caption("Map Viewer")
    pygame.init()
    
    def drawMoon(screen):
        global o
        tile = 4
        w = o.Width
        for x in range(w):
            for y in range(w):
                r = o.Sectors[x][y]
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
                
                pygame.draw.rect(screen, c, Rect(x*tile, y*tile, tile, tile ), 0) 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                keystate = pygame.key.get_pressed()
                if keystate[K_a]==1:
                    o = MoonModel(128)
                    o.Generate()
                    drawMoon(screen)
                elif keystate[K_p]==1:
                    xmoon = o.Save()
                    f = open('workfile', 'w')
                    f.write(xmoon)
                    f.close()
                    print("Saved.")
                elif keystate[K_o]==1:
                    f = open('workfile', 'r')
                    xmoon = f.read()
                    f.close()
                    o = jsonpickle.decode(xmoon)
                    drawMoon(screen)
                    print("Loaded.")
                if keystate[K_ESCAPE]==1:
                    sys.exit()
        pygame.display.update()
