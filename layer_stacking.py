import pygame
import math
pygame.font.init()
import os 
from os import *

SCREEN = pygame.display.set_mode((800,800),vsync=1)
pygame.display.set_caption("Sprite stacking")
DARK_GREY = (20,20,20)
WHITE = (255,255,255)
SCALE = 300
TARGET_FPS = 60
font = pygame.font.Font('fonts\ARIALBD 1.TTF',24)
clock = pygame.time.Clock()

class Kart_layer(pygame.sprite.Sprite):
    def __init__(self,image,spacing):
        super(Kart_layer,self).__init__()
        self.image = image
        self.surface = self.image
        self.rect = self.image.get_rect(center=(self.image.get_width(),self.image.get_height()))
        self.rect.x = SCREEN.get_width()/2 - (SCALE/2)
        self.rect.y = 400 + int(-(SCALE/ 90)*spacing)
        self.angle = 70
        self.image = pygame.transform.rotate(self.image,self.angle)

    def rotate(self):
        self.surface = pygame.transform.rotate(self.image,self.angle)
        self.rect = self.surface.get_rect(center=(self.rect.center))
        self.angle = self.angle % 360
        
#C:\Users\ztdnz\Desktop\Code files\Kart shifters\Kart1
#x = listdir("/Users/ztdnz/Desktop/Code files/Kart shifters/Kart1")

layers = listdir((os.path.abspath('Kart').replace("\\","/").removeprefix("C:").removesuffix("/Kart shifters")))
print(layers)

for png in enumerate(layers):
    png_number = png[0]
    png_name = png[1]
    layers[png_number] = "Kart/" + png_name

kart_layers = pygame.sprite.LayeredUpdates()

for layer in enumerate(layers):
    kart_layers.add(Kart_layer(pygame.transform.smoothscale(pygame.image.load(layer[1]).convert_alpha(),(SCALE,SCALE)),layer[0]))

all_sprite = kart_layers.get_sprite(9)

def fps_counter():
    fps = str(int(clock.get_fps()))
    fps_text = font.render((str("Fps: ")+ str(fps)) , True, pygame.Color(WHITE))
    fps_rect = fps_text.get_rect(center=(70,50))
    SCREEN.blit(fps_text,fps_rect)
Test_num = 0
run = True
while run:
    SCREEN.fill(DARK_GREY)
    clock.tick(TARGET_FPS)
    fps_counter()

    Test_num +=1
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    for layer in enumerate(layers):
        rotated_layer = kart_layers.get_sprite(layer[0])
        SCREEN.blit(rotated_layer.surface,rotated_layer.rect)
        rotated_layer.angle -= .2
        rotated_layer.rotate() 
        rotated_layer.rect.y = rotated_layer.rect.y - (math.sin(math.radians(Test_num)%SCALE)) * (layer[0]/1.9)

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            rotated_layer.rect.y -=layer[0]
        if keys[pygame.K_s]:
            rotated_layer.rect.y +=layer[0]
        
        if keys[pygame.K_a]:
            rotated_layer.rect.x -=1 
        if keys[pygame.K_d]:
            rotated_layer.rect.x +=1 
  

    pygame.display.update()

    
pygame.quit()


