#Importings
import pygame
import random

#Initialization
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("CaXeL")
clock = pygame.time.Clock()
in_game = True

#Sound
theme = pygame.mixer.Sound("music.mp3")
theme.play(-1)
click = pygame.mixer.Sound("click.mp3")
hover = pygame.mixer.Sound("hover.mp3")

#Game
class Game:
    def __init__(self):
        
        #Display
        self.bg = pygame.image.load("sprites/menu.png")
        self.in_menu = True
        self.playing = False
        self.editing = False
        self.controls = False
        
        #Keys
        self.mkey1 = pygame.K_g
        self.mkey2 = pygame.K_h
        self.mkey3 = pygame.K_k
        self.mkey4 = pygame.K_l
        self.okey1 = pygame.K_s
        self.okey2 = pygame.K_d

        #MISC
        self.snow = []
        for i in range(160):
            x = random.randrange(0, screen_width)
            y = random.randrange(0, screen_height)
            self.snow.append([x, y])
        
        #Sounds
        self.hoverplayed = False
        self.clickplayed = False
    
    def snowfall(self):
        for i in range(len(self.snow)):
            pygame.draw.circle(screen, (255,255,255), self.snow[i], random.randrange(1, 4))
            self.snow[i][1] += 0.3
            if self.snow[i][1] > screen_height:
                newy_pos = random.randrange(-50, -10)
                self.snow[i][1] = newy_pos
                newx_pos = random.randrange(0, screen_width)
                self.snow[i][0] = newx_pos

    def menu_screen(self):
        mouse = pygame.mouse.get_pos()
        played = False
        if 282 <= mouse[0] <= 325 and 422 <= mouse[1] <= 458:
            self.bg = pygame.image.load("sprites/settings.png")
            hover.play() if not self.hoverplayed else None
            self.hoverplayed = True
        elif 362 <= mouse[0] <= 406 and 422 <= mouse[1] <= 458:
            self.bg = pygame.image.load("sprites/play.png")
            hover.play() if not self.hoverplayed else None
            self.hoverplayed = True
        elif 442 <= mouse[0] <= 485 and 422 <= mouse[1] <= 458: 
            self.bg = pygame.image.load("sprites/create.png")
            hover.play() if not self.hoverplayed else None
            self.hoverplayed = True
        else: 
            self.bg = pygame.image.load("sprites/menu.png")
            self.hoverplayed = False
        screen.blit(self.bg, (0,0))
        if pygame.mouse.get_pressed()[0]:
                if 282 <= mouse[0] <= 325 and 422 <= mouse[1] <= 458:
                    click.play() if not self.clickplayed else None
                    self.clickplayed = True
                    self.in_menu = False
                    self.controls = True
                    pygame.mixer.fadeout(1000)
                elif 362 <= mouse[0] <= 406 and 422 <= mouse[1] <= 458: 
                    click.play() if not self.clickplayed else None
                    self.clickplayed = True
                    self.in_menu = False
                    self.playing = True
                    pygame.mixer.fadeout(1000)
                elif 442 <= mouse[0] <= 485 and 422 <= mouse[1] <= 458:
                    click.play() if not self.clickplayed else None
                    self.clickplayed = True
                    self.in_menu = False
                    self.editing = True 
                    pygame.mixer.fadeout(1000)
                else:
                    self.clickplayed = False
        self.snowfall()

    def gameplay(self):
        screen.fill((0,0,0))
        keys = pygame.key.get_pressed()
        lane = pygame.image.load("sprites/lane.png")
        lane_pressed = pygame.image.load("sprites/lane_pressed.png")
        lane_pos = [screen_width//4.5, screen_height - lane.get_height()]
        lane1 = lane_pressed if keys[self.mkey1] else lane
        lane2 = lane_pressed if keys[self.mkey2] else lane
        lane3 = lane_pressed if keys[self.mkey3] else lane
        lane4 = lane_pressed if keys[self.mkey4] else lane
        screen.blit(lane1, lane_pos)
        screen.blit(lane2, [lane_pos[0] + lane.get_width(), lane_pos[1]])
        screen.blit(lane3, [lane_pos[0] + lane.get_width()*2, lane_pos[1]])
        screen.blit(lane4, [lane_pos[0] + lane.get_width()*3, lane_pos[1]])

    def settings(self):
        self.bg = pygame.image.load("sprites/background.png")
        font = pygame.font.Font(('Assassin$.ttf'), 50)
        screen.blit(self.bg, (0,0))

        mouse = pygame.mouse.get_pos()
        
        #Texts
        title_Control = font.render("Controls", True, (255,255,255))
        screen.blit(title_Control, (74,53))

        back_button = font.render("Back", True, (255,255,255))
        screen.blit(back_button, mouse)


    def update(self):

       #Check Where Player is in game
        if self.in_menu:
            self.menu_screen()
        elif self.playing:
            self.gameplay()
        elif self.controls:
            self.settings()
      

game = Game()

#Game Code
while in_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    game.update()
    pygame.display.update()
    clock.tick(60)
