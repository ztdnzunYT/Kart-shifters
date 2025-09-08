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
    TARGET_FPS = 30
    START_Y = 400
    WHITE_COLOR = (255,255,255)
    BLACK_COLOR = (0,0,0)
    GAME_STATE = "Loading_screen"
    delta_time = clock.get_time() / 1000

class LoadingScreen:

    NUM_OF_SQUARES = 15 
    parallax_squares = []

    class ParallaxSquare():

        def __init__(self,start_x,start_y,image):
            self.start_x = start_x
            self.start_y = start_y
            self.image = pygame.transform.smoothscale((pygame.image.load(image).convert_alpha()),(200,200))
            self.rect = self.image.get_rect(topleft=(start_x,start_y))


class MainMenu:

    for i in range(5):
        for j in range(4):
            new_square = LoadingScreen.ParallaxSquare((i*200)-200,(j*200)-200,"assets//Passing lane background scroll.png")
            LoadingScreen.parallax_squares.append(new_square)



    print(LoadingScreen.parallax_squares)

    def drawBackgroundDisplay():
        for square in LoadingScreen.parallax_squares:
            SCREEN.blit(square.image,square.rect)

    def playBackgroundDisplay():
        for square in LoadingScreen.parallax_squares:
            if square.rect.x > SCREEN_WIDTH:
                square.rect.x = -200
            else:
                square.rect.x += 1

            if square.rect.y > SCREEN_HEIGHT:
                square.rect.y = -200
            else:
                square.rect.y +=1






def fps_counter():
    fps = str(int(clock.get_fps()))
    fps_text = font.render((str("Fps: ")+ str(fps)) , True, pygame.Color(Globals.WHITE_COLOR))
    fps_rect = fps_text.get_rect(center=(70,50))
    SCREEN.blit(fps_text,fps_rect)
 






run = True
while run:
    SCREEN.fill(Globals.BLACK_COLOR)
    clock.tick(Globals.TARGET_FPS)
    #SCREEN.blit(parking_lot,parking_lot_rect)



    MainMenu.drawBackgroundDisplay()
    MainMenu.playBackgroundDisplay()






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


