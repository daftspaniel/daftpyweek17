import random
import pygame
from pygame.locals import *

def CreateBackground(screen):
    bg = pygame.Surface(screen.get_size())
    bg = bg.convert()
    return bg

def DrawText(bg, x, y, text, size=24, color=(255, 255, 255)):
    inst1_font = pygame.font.Font(None, size)
    inst1_surf = inst1_font.render(text, 1, color)
    bg.blit(inst1_surf, [x, y])

def RND(num):
    return random.randint(1,num)
    
def randomPlusMinus1():
    n = random.randint(0,2)
    n -= 1
    return n
