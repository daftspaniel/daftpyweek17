'''
Game main module.

Contains the entry point used by the run_game.py script

'''

import sys
import pygame
from pygame.locals import *
from gamelib.util import *

# Globals.
ScreenSize = [640,480]
Debug = False

# Standard Init.
pygame.init()
screen = pygame.display.set_mode(ScreenSize)
pygame.display.set_caption("Moon")
ANIMEVENT = pygame.USEREVENT+3
DAYEVENT = pygame.USEREVENT+4
pygame.time.set_timer(ANIMEVENT, int(1000))
pygame.time.set_timer(DAYEVENT, int(60 * 1000))
surface = CreateBackground(screen)

#------
# MAIN
#------
def main():
    GameState = 1
    DrawText(surface, 10, 50, "Daftspaniel Presents...", 48, (255,255,255) )
    screen.blit(surface, (0, 0))
    pygame.display.flip()

    while GameState!=-1:

        if GameState == 1: # Title Screen
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
                elif event.type == ANIMEVENT:
                    surface.fill(pygame.Color("black"))
                    DrawText(surface, 10, 50, "Moon", 48, (255,0,0) )
                    DrawText(surface, 11, 51, "Moon", 48, (255,156,0) )
                    DrawText(surface, 11, 51, "Moon", 48, (255,255,255) )

                elif event.type == pygame.KEYDOWN:
                    keystate = pygame.key.get_pressed()
                    if keystate[K_SPACE]:
                        GameState = 2

            screen.blit(surface, (0, 0))
            pygame.display.flip()

        elif GameState == 2: # Game on!
            
            print("Game on")
            surface.fill(pygame.Color("black"))
            DrawText(surface, 10, 50, "Creating Your Moon...", 48, (255,0,0) )
            screen.blit(surface, (0, 0))
            pygame.display.flip()
            #GameMs = MadScience(GameBG, screen, ScreenSize)
            #GameMs.MainLoop()


            #if GameMs.P1.Health<1:
            #GameState = 3
            #else:
            #GameState = 4

        elif GameState == 3: # Game over!
        
            surface.fill(pygame.Color("black"))
            DrawText(surface, 10, 50, "Game Over", 48, (255,0,0) )
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    keystate = pygame.key.get_pressed()
                    if keystate[K_SPACE]:
                        GameState = 1
            screen.blit(surface, (0, 0))
            pygame.display.flip()

        elif GameState == 4: # Game Win

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == ANIMEVENT:
                    surface.fill(pygame.Color("black"))
                    DrawText(surface, 10, 50, "Well Done!", 48, (255,0,0) )
                    
                elif event.type == pygame.KEYDOWN:
                    keystate = pygame.key.get_pressed()
                    if keystate[K_SPACE]:
                        GameState = 1
                        
            screen.blit(GameBG, (0, 0))
            pygame.display.flip()
