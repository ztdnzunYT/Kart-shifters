import pygame  #may need to use pip install pygame
import math
pygame.font.init()
pygame.mixer.init()
import random
from os import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),vsync=1)
pygame.display.set_caption("PassingLane")

font = pygame.font.Font('fonts\\lightsideracad.ttf',24)
clock = pygame.time.Clock()

class Globals:
    
    SCALE = 50
    TARGET_FPS = 60
    START_Y = 400
    WHITE_COLOR = (255,255,255)
    BLACK_COLOR = (0,0,0) 
    GAME_STATES = ["loading_screen","main_menu","test_scale"]
    GAME_STATE = "main_menu"
    delta_time = clock.get_time() / 1000
    input_device = "pc"

class LoadingScreen:

    NUM_OF_SQUARES = 15 
    TIME_DELAY = 25
    time = pygame.time.get_ticks()
    parallax_squares = []
    transition = False
    transition_amount = 255

    class ParallaxSquare():

        def __init__(self,start_x,start_y,image):
            self.start_x = start_x
            self.start_y = start_y
            self.surface = pygame.transform.smoothscale((pygame.image.load(image).convert_alpha()),(200,200))
            self.rect = self.surface.get_rect(topleft=(start_x,start_y))
            self.transparency = 255

    def checkTransitionGameState():
        if LoadingScreen.transition == True:
            LoadingScreen.transition_amount = max(LoadingScreen.transition_amount-3,0)
        if LoadingScreen.transition_amount <=0:
            LoadingScreen.transition == False
            Globals.GAME_STATE = "main_menu"
 
        #print(LoadingScreen.transition,Globals.GAME_STATE)

class StartUpScreen:

    passing_lane_coverart_png = pygame.transform.smoothscale(pygame.image.load("assets\\cover_art.png").convert_alpha(),(700/1.2,400/1.2)) 
    passing_lane_cover_rect = passing_lane_coverart_png.get_rect(center=(passing_lane_coverart_png.get_size()[0]/2,passing_lane_coverart_png.get_size()[1]/2))
    passing_lane_cover_rect.x  = SCREEN_WIDTH/2 - passing_lane_cover_rect.size[0]/2.05
    passing_lane_cover_velocity = -6

    if Globals.input_device == "pc":
            text = "space"
    elif Globals.input_device == "controller":
        text = "x"

    play_text = font.render((f"Press {text} to start"),True, pygame.Color(255,255,255,))
    play_rect = play_text.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2+50))
    play_rect_transparency = 255

    @staticmethod
    def CreateSquares():
        for i in range(6):
            for j in range(4):
                new_square = LoadingScreen.ParallaxSquare((i*200)-350,(j*200)-200,"assets\\Passing lane background scroll.png")
                LoadingScreen.parallax_squares.append(new_square)

    CreateSquares()

    def drawBackgroundDisplay():
        for square in LoadingScreen.parallax_squares:
            square.surface.set_alpha(square.transparency)
            if LoadingScreen.transition == True:
                square.transparency = max(square.transparency-4,0)
                

            SCREEN.blit(square.surface,square.rect)

    def playBackgroundDisplay():
        current_time = pygame.time.get_ticks()

        if current_time > LoadingScreen.time:
            
            for square in LoadingScreen.parallax_squares:
                if square.rect.x > SCREEN_WIDTH+48:
                    square.rect.x = -350
                else:
                    square.rect.x += 1

                if square.rect.y > SCREEN_HEIGHT+98:
                    square.rect.y = -200
                else:
                    square.rect.y +=1

            LoadingScreen.time = current_time + LoadingScreen.TIME_DELAY

    def drawStartupLogo():

        if LoadingScreen.transition == False:
          StartUpScreen.passing_lane_cover_rect.y = 10 * math.sin((math.pi * .5 * pygame.time.get_ticks()/1000)) + 85
        
        if LoadingScreen.transition == True:
            StartUpScreen.passing_lane_cover_velocity +=.5
            if StartUpScreen.passing_lane_cover_rect.y > -250:
                StartUpScreen.passing_lane_cover_rect.y -= StartUpScreen.passing_lane_cover_velocity
        
        SCREEN.blit(StartUpScreen.passing_lane_coverart_png,(StartUpScreen.passing_lane_cover_rect))
        
    def drawPlayButton():
        StartUpScreen.play_rect.y = 5 * math.sin((math.pi * .5 * pygame.time.get_ticks()/1000)) + 310
        if LoadingScreen.transition == False:
            transparency = (int(abs(230 * math.sin((math.pi*.1*pygame.time.get_ticks()/1000)))))
            StartUpScreen.play_text.set_alpha(transparency)
            StartUpScreen.play_rect_transparency = transparency
        else:
            StartUpScreen.play_rect_transparency = max(StartUpScreen.play_rect_transparency-3,0)
            StartUpScreen.play_text.set_alpha(StartUpScreen.play_rect_transparency)
        
        SCREEN.blit(StartUpScreen.play_text,StartUpScreen.play_rect)

class MainMenu: 

    class SideMenu:
        menu_options_text = ["Cruise","Garage","Compete","Settings"]
        menu_options = []
        selected_option = 0
        options_y_offset = 65
        options_x_end = 40

        actions = {
            pygame.K_w: lambda: MainMenu.SideMenu.getSelectedOption("up"),
            pygame.K_s: lambda: MainMenu.SideMenu.getSelectedOption("down")
        }

        def getSelectedOption(direction):

            if direction == "up":
                MainMenu.SideMenu.selected_option -=1 

                if MainMenu.SideMenu.selected_option < 0: 
                    MainMenu.SideMenu.selected_option = len(MainMenu.SideMenu.menu_options_text) -1

            if direction == "down": 
                MainMenu.SideMenu.selected_option +=1

                if MainMenu.SideMenu.selected_option > len(MainMenu.SideMenu.menu_options_text) -1:
                    MainMenu.SideMenu.selected_option = 0

        def drawMenuOptions():

            for option in enumerate(MainMenu.SideMenu.menu_options) :

                index = option[0]
                sidemenu_option = option[1]

                sidemenu_option.y = sidemenu_option.start_y + index * MainMenu.SideMenu.options_y_offset
                sidemenu_option.rect.y = sidemenu_option.y

                if sidemenu_option.rect.x < MainMenu.SideMenu.options_x_end + index *10 and Globals.GAME_STATE == "main_menu":
                    sidemenu_option.slide_velocity +=1
                    sidemenu_option.rect.x = min(sidemenu_option.rect.x + sidemenu_option.slide_velocity,MainMenu.SideMenu.options_x_end + index * 3) 

                sidemenu_option.transparency = sidemenu_option.text.get_alpha()
            
                if sidemenu_option.label == MainMenu.SideMenu.menu_options_text[MainMenu.SideMenu.selected_option]:
                    sidemenu_option.text.set_alpha(min(sidemenu_option.transparency+10,255))
                    sidemenu_option.y = sidemenu_option.y + 3 * math.sin(2*math.pi*.8*pygame.time.get_ticks()/1500)
                    sidemenu_option.rect.y = sidemenu_option.y
                else:
                    sidemenu_option.text.set_alpha(max(sidemenu_option.transparency-10,sidemenu_option.set_transparency))

                SCREEN.blit(sidemenu_option.text,sidemenu_option.rect)

    class SideMenuOption:
        text_size = 30

        def __init__(self,x,y,text,size):
            self.x = x
            self.y = y 
            self.start_y = y
            self.size = size
            self.slide_velocity = .8
            self.font = pygame.font.Font('fonts\\lightsider.ttf',self.size)
            self.label = text
            self.text = self.font.render(text,True,(255,255,255))
            self.rect = self.text.get_rect(topleft=(x,y))
            self.set_transparency = 150
            self.transparency = 255
    
    for option in SideMenu.menu_options_text:
        SideMenu.menu_options.append(SideMenuOption(-200,40,str(option),SideMenuOption.text_size))

    class SoundEffects():
        pygame.mixer.set_num_channels(8)

class CrusieGameMode:

    class Player:
        def __init__(self,x,y,image,layers,name,top_speed,handling,acceleration,brake):
            self.x = x 
            self.y = y
            self.pos_x = 0
            self.pos_y = 0
            self.layers = layers
            self.image = image
            self.surface = pygame.image.load(self.image).convert_alpha()
            self.angle = 0
            self.rotated_surface = None
            self.rect = self.image.get_rect()
            self.speed = 0
            self.name = name 
            self.top_speed = top_speed
            self.handling = handling 
            self.acceleration = acceleration
            self.brake = brake
            self.health = 0
            self.x_vel = 0
            self.y_vel = 0 
        
    class Road:

        road_types = {
            "default_highways" : {"straight":"assets\\roads\\default_straight_road1.png"},
        }

        roads = []
        
        def __init__(self,x,y,y_vel,road_types):
            self.x = x
            self.y = y  
            self.y_vel = y_vel
            self.roads = road_types
            self.surface = pygame.transform.smoothscale_by(pygame.image.load(self.road_types["default_highways"]["straight"]).convert_alpha(),.3)
            self.rect = self.surface.get_rect(topleft=(0,0))


            
        def drawRoad():
            for road in CrusieGameMode.Road.roads:
                SCREEN.blit(road.surface,road.rect)
                road.rect.y+= 2

                if road.rect.y > road.surface.get_size()[1] :
                    road.rect.y = -road.surface.get_size()[1]
        

            

    def drawPlayerBoundingUi():
            pygame.draw.rect(CrusieGameMode.playerBoundingSurface,(255,0,0),CrusieGameMode.playerBoundingBox,1)
            SCREEN.blit(CrusieGameMode.playerBoundingSurface,(SCREEN_WIDTH/1.2-CrusieGameMode.playerBoundingBox.size[0],SCREEN_HEIGHT/3))

    playerBoundingSurface = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.SRCALPHA)
    playerBoundingSurface.fill((255,255,255,0))
    playerBoundingBox = pygame.Rect(0,0,SCREEN_WIDTH/1.5,SCREEN_HEIGHT/2)

    for i in range(4):
        Road.roads.append(Road(0,0,0,Road.road_types["default_highways"]["straight"]))
    
    for object in enumerate(Road.roads):
        index  = object[0]
        road = object[1]   

        road.rect.x = (index * road.surface.get_size()[0]/2.5)
        road.rect.y = (index * road.surface.get_size()[1])
      

 

    

class TestScale:

    class Camera:
        actions = {
            pygame.K_w: lambda: TestScale.cameraScale("up"),
            pygame.K_s: lambda: TestScale.cameraScale("down")
        }

        startScale = 1
        globalScale = 0
        globalScaleMultipier = 2.5

    class MyRect:

        def __init__(self,x,y,width,height,color):
            self.x = x 
            self.y = y 
            self.start_x = self.x
            self.start_y = self.y 
            self.width = width 
            self.height = height
            self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
            self.color = color

    class OtherRectangle:

        def __init__(self,x,y,width,height,color):
            self.x = x 
            self.y = y 
            self.start_x = self.x
            self.start_y = self.y 
            self.width = width 
            self.height = height
            self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
            self.color = color

    def drawRects():
        for otherRects in TestScale.otherRects:
            pygame.draw.rect(SCREEN,TestScale.myRect.color,TestScale.myRect.rect,1)
            pygame.draw.rect(SCREEN,otherRects.color,otherRects.rect,1)

    def cameraScale(scale_direction):
                
        TestScale.Camera.globalScale +=1 if scale_direction == "up" else -1 if scale_direction == "down" else None #INCREASES CAMERA GLOBAL SCALE OF BUTTON PRESS UP OR DOWN 
        
        for otherRects in TestScale.otherRects:

            xOrientationVal = -1 if TestScale.myRect.x > otherRects.x else 1 if TestScale.myRect.x < otherRects.x else 0 #DETERMINES WHAT SIDE THE RECTANGLE IS ON IN RELATION TO MYRECT
            yOrientationVal = 1 if TestScale.myRect.y > otherRects.y else -1 if TestScale.myRect.y < otherRects.y else 0 #DETERMINES WHAT SIDE THE RECTANGLE IS ON IN RELATION TO MYRECT
            
            otherRects.x +=(TestScale.Camera.globalScaleMultipier*xOrientationVal) if scale_direction == "up" else (-TestScale.Camera.globalScaleMultipier*xOrientationVal) if scale_direction == "down" else None #ALLOWS THE OTHER RECTANGLES TO MOVE IN CERTAIN DIRECTION WITH SCALE IN ORIENTATION TO MY RECT 
            otherRects.y +=(-TestScale.Camera.globalScaleMultipier*yOrientationVal) if scale_direction == "up" else (TestScale.Camera.globalScaleMultipier*yOrientationVal) if scale_direction == "down" else None #ALLOWS THE OTHER RECTANGLES TO MOVE IN CERTAIN DIRECTION WITH SCALE IN ORIENTATION TO MY RECT 

            TestScale.myRect.rect = pygame.Rect(TestScale.myRect.x-TestScale.Camera.globalScale/2,
                                                TestScale.myRect.y-TestScale.Camera.globalScale/2,
                                                TestScale.myRect.width + TestScale.Camera.globalScale,
                                                TestScale.myRect.height + TestScale.Camera.globalScale)

            otherRects.rect = pygame.Rect(otherRects.x-TestScale.Camera.globalScale/2,
                                                otherRects.y-TestScale.Camera.globalScale/2,
                                                otherRects.width + TestScale.Camera.globalScale,
                                                otherRects.height + TestScale.Camera.globalScale)


    myRect = MyRect(SCREEN_WIDTH/2-25,SCREEN_HEIGHT/2+50,35,50,(255,255,255))
    otherRect1 = OtherRectangle(600,SCREEN_HEIGHT/2+50,35,50,(255,255,255))
    otherRect2 = OtherRectangle(100,SCREEN_HEIGHT/2+50,35,50,(255,255,255))
    otherRects = [otherRect1,otherRect2]


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
        StartUpScreen.drawBackgroundDisplay()
        StartUpScreen.playBackgroundDisplay()
        StartUpScreen.drawPlayButton()
        StartUpScreen.drawStartupLogo() 
        LoadingScreen.checkTransitionGameState()
    

    if Globals.GAME_STATE == "main_menu": 
        SCREEN.fill((80,80,80))
        CrusieGameMode.Road.drawRoad()
        CrusieGameMode.drawPlayerBoundingUi()
        MainMenu.SideMenu.drawMenuOptions()
        TestScale.drawRects()
        
        
    if Globals.GAME_STATE == "test_scale":
        pass

        

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                LoadingScreen.transition = True
            
            if Globals.GAME_STATE == "main_menu":
                if event.key in MainMenu.SideMenu.actions:
                    MainMenu.SideMenu.actions[event.key]()
                    TestScale.Camera.actions[event.key]()

           
             


    keys = pygame.key.get_pressed()
    fps_counter()

    pygame.display.update()


    
pygame.quit()
