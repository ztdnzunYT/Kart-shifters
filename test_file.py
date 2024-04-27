import pygame
import math
 
clock = pygame.time.Clock()
pygame.display.set_caption("Test drifting")
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY  =(150,150,150)
TARGET_FPS = 60
SW = 800
SH = 800
screen = pygame.display.set_mode((SW,SH))

class Car(pygame.sprite.Sprite):
    def __init__(self,rotation_val):
        super(Car,self).__init__()
        self.image = pygame.transform.smoothscale(pygame.image.load('Indigo kart model\sprite_01.png').convert_alpha(),(100,100))
        self.surf = self.image 
        self.angle  = 0
        self.surf = pygame.transform.rotate(self.image,self.angle)
        self.rect = self.surf.get_rect(center=(self.surf.get_width()/2,self.surf.get_height()/2))
        self.rect.center = (SW/2,SH/2)
        self.max_rotation_val = 3
        self.rotation_val = rotation_val
        self.drift_value = self.angle
        self.velocity = 0.5
        self.max_velocity = 5
        self.acceleration = 0.008

    def rotate(self,left=False,right=False):
        if car1.velocity > 0.6:
            if left: 
                self.angle += self.rotation_val
            if right:
                self.angle += -self.rotation_val

        if keys[pygame.K_LSHIFT] == False:
            if keys[pygame.K_a]:
                if self.drift_value > self.angle:
                    self.drift_value -=1

        if keys[pygame.K_LSHIFT] == False: 
            
            if self.drift_value + self.angle > self.angle:
                self.drift_value -=5

            if right:
                self.surf = pygame.transform.rotate(self.image,self.angle - self.drift_value)
                self.rect = self.surf.get_rect(center=(self.rect.center))
                self.angle = self.angle % 360
            if left:
                self.surf = pygame.transform.rotate(self.image,self.angle - -self.drift_value)
                self.rect = self.surf.get_rect(center=(self.rect.center))
                self.angle = self.angle % 360
        else:
            if self.drift_value <=50:
                self.drift_value +=1


            if self.velocity > 0.5:
                if right == False and left: 
                    self.surf = pygame.transform.rotate(self.image,self.angle + self.drift_value)
                    self.rect = self.surf.get_rect(center=(self.rect.center))
                    self.angle = self.angle % 360
                if left == False and right:
                    self.surf = pygame.transform.rotate(self.image,self.angle + -self.drift_value)
                    self.rect = self.surf.get_rect(center=(self.rect.center))
                    self.angle = self.angle % 360

                if left and right:
                    self.surf = pygame.transform.rotate(self.image,self.angle )
                    self.rect = self.surf.get_rect(center=(self.rect.center))
                self.angle = self.angle % 360


    def move_foward(self):
        self.velocity = min((self.velocity + self.acceleration),self.max_velocity)
        self.turn(foward=True)
    
    def brake(self):
        if self.velocity > 1:
            self.velocity -=0.02
        

    def turn(self,foward=False,backward=False):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.velocity 
        horizontal = math.sin(radians) * self.velocity
        if foward: 
            self.rect.x -= horizontal
            self.rect.y -= vertical 
           
       
car1 = Car(3)

run = True
while run:

    clock.tick(TARGET_FPS)
    screen.fill(GREY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    
    keys = pygame.key.get_pressed()

    print(car1.velocity)
    if keys[pygame.K_w]:
        car1.move_foward()
    elif keys[pygame.K_w] == False:
        if car1.velocity >= 0.5:
            car1.move_foward()
            car1.velocity -= 0.02
    if keys[pygame.K_s]:
        car1.brake()
    if keys[pygame.K_a]:
        car1.rotate(left=True) 
    if keys[pygame.K_d]:
        car1.rotate(right=True)
        

    if keys[pygame.K_LSHIFT]:
        car1.rotation_val = 1.5
        car1.velocity - 0.05
    else:
        car1.rotation_val =3
    

 
    

    


        



    screen.blit(car1.surf,car1.rect)
    pygame.display.flip()





pygame.quit()