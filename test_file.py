import pygame  #may need to use pip install pygame
import math
pygame.font.init()
import os 
from os import *

SCREEN = pygame.display.set_mode((750,750),vsync=1)
pygame.display.set_caption("Sprite stacking")
DARK_GREY = (20,20,20)
WHITE = (255,255,255)
GRASS_COLOR = (97,137,55) 
SCALE = 100
TARGET_FPS = 60
font = pygame.font.Font('fonts/ARIALBD 1.TTF',24)
clock = pygame.time.Clock()
START_Y = 400


parking_lot = pygame.transform.smoothscale(pygame.image.load('basic map\sprite_0.png').convert_alpha(),(1500,1500))
parking_lot_rect = parking_lot.get_rect(center=(parking_lot.get_width()/2,parking_lot.get_height()/2))
parking_lot_rect.center = (SCREEN.get_width()/2,SCREEN.get_height()/2)
parking_lot_rect.x = 0



class Kart_layer(pygame.sprite.Sprite):
    def __init__(self,image,spacing):
        super(Kart_layer,self).__init__()
        self.image = image
        self.surface = self.image
        self.rect = self.image.get_rect(center=(self.image.get_width(),self.image.get_height()))
        self.rect.x = SCREEN.get_width()/2 - (SCALE/2)
        self.rect.y = START_Y + int(-(SCALE/ 90)*spacing)
        self.angle = 90
        self.velocity = 0.5
        self.max_velocity = 6
        self.rotation_val = 1.5
        self.max_rotation = 3
        self.acceleration = 0.008
        self.image = pygame.transform.rotate(self.image,self.angle)
        self.surface = pygame.transform.rotate(self.image,self.angle)
        self.drift_val = 0
        self.drift_max = 50
    
      
    def rotate(self,left=False,right=False):
        if self.velocity > 0.6 and keys[pygame.K_w]:
            if left: 
                self.angle += self.rotation_val
            if right:
                self.angle += -self.rotation_val

        if keys[pygame.K_LSHIFT] == False:
            if self.drift_val > 0:
                self.drift_val -=2.5
            elif self.drift_val < 0:
                self.drift_val +=2.5

            self.surface = pygame.transform.rotate(self.image,self.angle - self.drift_val)
        else:
            self.surface = pygame.transform.rotate(self.image,self.angle - self.drift_val)
        self.rect = self.surface.get_rect(center=(self.rect.center))
        self.angle = self.angle % 360


    def move(self,foward=False,backward=False):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.velocity 
        horizontal = math.sin(radians) * self.velocity
        if foward:
            self.velocity = min((self.velocity + self.acceleration),self.max_velocity)
            self.rect.x -= horizontal
            self.rect.y -= vertical 
    
    def brake(self):
        if self.velocity > .5 :
            self.velocity -=.02

    def drift(self):  
        if self.velocity > .5 :
            self.velocity -= 0.015
        self.rotation_val = 1.5
        if self.drift_val > -self.drift_max:
            if keys[pygame.K_a]: 
                self.drift_val -=1
        if self.drift_val < self.drift_max:
            if keys[pygame.K_d]:
                self.drift_val +=1
        return self.drift_val
   
    
#C:\Users\ztdnz\Desktop\Code files\Kart shifters\Kart1
#x = listdir("/Users/ztdnz/Desktop/Code files/Kart shifters/Kart1")

kart_model = str('red kart model\\red kart images')
layers = listdir(kart_model)


layers.sort(reverse=False)
print(layers)

for png in enumerate(layers):
    png_number = png[0]
    png_name = png[1]
    layers[png_number] = kart_model + "/" + png_name

kart_layers = pygame.sprite.LayeredUpdates()

for layer_num,layer_name in enumerate(layers):
    kart_layers.add(Kart_layer(pygame.transform.smoothscale(pygame.image.load(layer_name).convert_alpha(),(SCALE,SCALE)),layer_num))

all_sprite = kart_layers.get_sprite(9)

def fps_counter():
    fps = str(int(clock.get_fps()))
    fps_text = font.render((str("Fps: ")+ str(fps)) , True, pygame.Color(WHITE))
    fps_rect = fps_text.get_rect(center=(70,50))
    SCREEN.blit(fps_text,fps_rect)
Test_num = 0

run = True
while run:
    SCREEN.fill(GRASS_COLOR)
    clock.tick(TARGET_FPS)
    SCREEN.blit(parking_lot,parking_lot_rect)


    Test_num +=0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    keys = pygame.key.get_pressed()

    for layer_num,layer_name in enumerate(layers):

        kart_layer = kart_layers.get_sprite(layer_num)   
        SCREEN.blit(kart_layer.surface,kart_layer.rect)
        
        if keys[pygame.K_w]:
            kart_layer.move(foward=True)
        elif keys[pygame.K_w] == False:
            if kart_layer.velocity >= 0.5:
                kart_layer.move(foward=True)
                kart_layer.velocity -= 0.02
        if keys[pygame.K_s]:
            kart_layer.brake()
        if keys[pygame.K_a]:
            kart_layer.rotate(left=True)
        if keys[pygame.K_d]:
            kart_layer.rotate(right=True)
        if keys[pygame.K_LSHIFT]:
            kart_layer.drift()
        else:
            if kart_layer.rotation_val < kart_layer.max_rotation:
                kart_layer.rotation_val += 0.5
        
        print(f"{kart_layer.velocity:.3f}")


        


     

    fps_counter()

     
 
  

    pygame.display.update()


    
pygame.quit()


