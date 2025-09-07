import pygame  #may need to use pip install pygame
import math
pygame.font.init()
from os import *

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 500
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),vsync=1)
pygame.display.set_caption("Sprite stacking")

font = pygame.font.Font('fonts/ARIALBD 1.TTF',24)
clock = pygame.time.Clock()

class Globals:
    
    SCALE = 50
    TARGET_FPS = 120
    START_Y = 400
    WHITE_COLOR = (255,255,255)
    BLACK_COLOR = (0,0,0)
    GAME_STATE = "Loading_screen"

class LoadingScreen:

    parallax_squares = []

    class ParallaxSquare():

        def __init__(self,x,y,image):
            self.x = x
            self.y = y
            self.image = pygame.transform.smoothscale((pygame.image.load(image).convert_alpha()),(200,200))
            self.rect = self.image.get_rect()

    
    parallax_square = ParallaxSquare(0,0,"assets//Passing lane background scroll.png")


class MainMenu:


    def playBackgroundDisplay():
        pass


print(LoadingScreen.parallax_square.rect.size)












def fps_counter():
    fps = str(int(clock.get_fps()))
    fps_text = font.render((str("Fps: ")+ str(fps)) , True, pygame.Color(Globals.WHITE_COLOR))
    fps_rect = fps_text.get_rect(center=(70,50))
    SCREEN.blit(fps_text,fps_rect)
 
for x in range(10): LoadingScreen.parallax_squares.append(LoadingScreen.parallax_square)





run = True
while run:
    SCREEN.fill(Globals.BLACK_COLOR)
    clock.tick(Globals.TARGET_FPS)
    #SCREEN.blit(parking_lot,parking_lot_rect)

    SCREEN.blit(LoadingScreen.parallax_square.image,LoadingScreen.parallax_square.rect)










  









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


