import pygame  #may need to use pip install pygame
import math
pygame.font.init()
from os import *

SCREEN = pygame.display.set_mode((750,750),vsync=1)
pygame.display.set_caption("Sprite stacking")

font = pygame.font.Font('fonts/ARIALBD 1.TTF',24)
clock = pygame.time.Clock()

class Globals:

    SCALE = 50
    TARGET_FPS = 120
    START_Y = 400
    WHITE_COLOR = (255,255,255)

def fps_counter():
    fps = str(int(clock.get_fps()))
    fps_text = font.render((str("Fps: ")+ str(fps)) , True, pygame.Color(Globals.WHITE_COLOR))
    fps_rect = fps_text.get_rect(center=(70,50))
    SCREEN.blit(fps_text,fps_rect)

run = True
while run:
    SCREEN.fill((115,115,115))
    clock.tick(Globals.TARGET_FPS)
    #SCREEN.blit(parking_lot,parking_lot_rect)

   






















    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False 

    keys = pygame.key.get_pressed()
    fps_counter()

     
 
  

    pygame.display.update()


    
pygame.quit()


