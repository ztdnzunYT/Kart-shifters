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
    TARGET_FPS = 60
    START_Y = 400
    WHITE_COLOR = (255,255,255)
    BLACK_COLOR = (0,0,0)
    GAME_STATE = "loading_screen"
    delta_time = clock.get_time() / 1000
    input_device = "pc"

class LoadingScreen:

    NUM_OF_SQUARES = 15 
    TIME_DELAY = 25
    time = pygame.time.get_ticks()
    parallax_squares = []

    class ParallaxSquare():

        def __init__(self,start_x,start_y,image):
            self.start_x = start_x
            self.start_y = start_y
            self.image = pygame.transform.smoothscale((pygame.image.load(image).convert_alpha()),(200,200))
            self.rect = self.image.get_rect(topleft=(start_x,start_y))



class MainMenu:
    
    @staticmethod
    def CreateSquares():
        for i in range(5):
            for j in range(4):
                new_square = LoadingScreen.ParallaxSquare((i*200)-200,(j*200)-200,"assets//Passing lane background scroll.png")
                LoadingScreen.parallax_squares.append(new_square)

    CreateSquares()

    def drawBackgroundDisplay():
        for square in LoadingScreen.parallax_squares:
            SCREEN.blit(square.image,square.rect)

    def playBackgroundDisplay():
        current_time = pygame.time.get_ticks()

        if current_time > LoadingScreen.time:
            
            for square in LoadingScreen.parallax_squares:
                if square.rect.x > SCREEN_WIDTH:
                    square.rect.x = -200
                else:
                    square.rect.x += 1

                if square.rect.y > SCREEN_HEIGHT:
                    square.rect.y = -200
                else:
                    square.rect.y +=1

            LoadingScreen.time = current_time + LoadingScreen.TIME_DELAY

    def draw_logo():

        passing_lane_coverart_png = pygame.transform.smoothscale(pygame.image.load("assets//cover_art.png").convert_alpha(),(700/1.2,400/1.2)) 
        passing_lane_cover_rect = passing_lane_coverart_png.get_rect(center=(passing_lane_coverart_png.get_size()[0]/2,passing_lane_coverart_png.get_size()[1]/2))
        passing_lane_cover_rect.center = (SCREEN_WIDTH/2+10,SCREEN_HEIGHT/2)

        passing_lane_cover_rect.y = 10 * math.sin((math.pi * .5 * pygame.time.get_ticks()/1000)) + 85
        SCREEN.blit(passing_lane_coverart_png,(passing_lane_cover_rect))
        
    def draw_play_button():
        if Globals.input_device == "pc":
            text = "space"
        elif Globals.input_device == "controller":
            text = "x"

        play_text = font.render((f"Press {text} to start"),True, pygame.Color(255,255,255,))
        play_rect = play_text.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2+50))

        play_rect.y = 5 * math.sin((math.pi * .5 * pygame.time.get_ticks()/1000)) + 310
        transparency = (int(abs(230 * math.sin((math.pi*.1*pygame.time.get_ticks()/1000)))))
        play_text.set_alpha(transparency)
        SCREEN.blit(play_text,play_rect)
 

def fps_counter():
    fps = str(int(clock.get_fps()))
    fps_text = font.render((str("Fps: ")+ str(fps)) , True, pygame.Color(Globals.WHITE_COLOR))
    fps_rect = fps_text.get_rect(center=(70,50))
    #SCREEN.blit(fps_text,fps_rect)
 

run = True
while run:
    SCREEN.fill(Globals.BLACK_COLOR)
    clock.tick(Globals.TARGET_FPS)

    if Globals.GAME_STATE == "loading_screen":
        MainMenu.drawBackgroundDisplay()
        MainMenu.playBackgroundDisplay()
        MainMenu.draw_logo()
        MainMenu.draw_play_button()



    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("key space preseed")



    keys = pygame.key.get_pressed()
    fps_counter()

     
 
  

    pygame.display.update()


    
pygame.quit()
