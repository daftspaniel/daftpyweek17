import pygame
import sys
from pygame.locals import *

Sky = [ Color(0,0,55), Color(50,0,145), Color(0,0,255) ]
Ground = [ Color(11,65,60), Color(17,155,80), Color(139,207,136)]
WoodGround = [ Color(41,65,60), Color(47,155,80), Color(169,207,136)]
Shore = [ Color(111,140,60), Color(151,180,0), Color(191,220,40)]
Water = [ Color(0,80,167), Color(17,113,207), Color(57,153,247)]
Tree = [ Color(0,145,0), Color(0,185,0), Color(0,205,0)]
Snow = [ Color(220,220,220), Color(240,240,240), Color(255,255,255)]
Fruit = [ Color(145,0,0), Color(185,0,0), Color(205,0,0)]

if __name__=="__main__":
    WINSIZE = 640,680
    
    pygame.init()
    screen = pygame.display.set_mode(WINSIZE,0,8)
    pygame.display.set_caption("Colour Palette for PyWeek17")
    pygame.init()

    y = 0
    w = 50
    ColourChart = [Sky, Ground, Tree, Fruit]
    for r in ColourChart:
        x = 0
        y += w
        for c in r:
            x += w
            pygame.draw.rect(screen, c, Rect(x, y, w, w ), 0)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
