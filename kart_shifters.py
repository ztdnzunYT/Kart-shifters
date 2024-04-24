import random
import pygame
from pygame.locals import (K_LEFT, K_RIGHT)

# Pygame initialization
pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Kart Shifters")
# Class for creating test object

class Wheel(pygame.sprite.Sprite):
    def __init__(self):
        super(Wheel,self).__init__()
        self.image = pygame.transform.smoothscale(pygame.image.load("Kart model\sprite_13.png").convert_alpha(), (500,500))
        self.image = pygame.transform.rotate(self.image,90)
        self.surface = self.image
        self.rect = self.surface.get_rect(center=(self.image.get_width()/2,self.image.get_height()/2))
        self.rect.x = 150
        self.rect.y = 150
        self.angle = 0
        self.change_angle = 0 
        self.layer = 0 

    def rotate(self):
        self.surface = pygame.transform.rotate(self.image,self.angle)
        self.angle += self.change_angle
        self.angle = self.angle % 360
        self.rect = self.surface.get_rect(center=(self.rect.center))




wheel1 = Wheel()
wheel2 = Wheel()

karts = pygame.sprite.Group()
karts.add(wheel1)
Red = (200,0,0)


# Main run loop
run = True
while run:
    # Screen fill
    screen.fill((130, 130, 130))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        wheel1.angle +=1
        wheel2.angle = wheel1.angle
    if keys[pygame.K_d]:
        wheel1.angle -=1
        wheel2.angle = wheel1.angle
    
    screen.blit(wheel1.surface,wheel1.rect)
    screen.blit(wheel2.surface,wheel2.rect)

    wheel2.rect.centerx = wheel1.rect.centerx + 100


  
    wheel1.rotate()
    wheel2.rotate()
    









    # Getting presses for move


    # Closing the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    # Rendering and rotating



    # Flipping and setting framerate
    
    pygame.display.flip()
    pygame.time.Clock().tick(120)

# Quit
pygame.quit() 