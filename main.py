#Importings
import pygame
import random
from moviepy.editor import VideoFileClip
import cv2


#Initialization
pygame.init()
screen_width = 1350
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("CaXeL")
clock = pygame.time.Clock()
in_game = True
character_mapping = {
    'a': pygame.K_a, 'b': pygame.K_b, 'c': pygame.K_c, 'd': pygame.K_d,
    'e': pygame.K_e, 'f': pygame.K_f, 'g': pygame.K_g, 'h': pygame.K_h,
    'i': pygame.K_i, 'j': pygame.K_j, 'k': pygame.K_k, 'l': pygame.K_l,
    'm': pygame.K_m, 'n': pygame.K_n, 'o': pygame.K_o, 'p': pygame.K_p,
    'q': pygame.K_q, 'r': pygame.K_r, 's': pygame.K_s, 't': pygame.K_t,
    'u': pygame.K_u, 'v': pygame.K_v, 'w': pygame.K_w, 'x': pygame.K_x,
    'y': pygame.K_y, 'z': pygame.K_z, '0': pygame.K_0, '1': pygame.K_1,
    '2': pygame.K_2, '3': pygame.K_3, '4': pygame.K_4, '5': pygame.K_5,
    '6': pygame.K_6, '7': pygame.K_7, '8': pygame.K_8, '9': pygame.K_9,
    ' ': pygame.K_SPACE, '.': pygame.K_PERIOD, ',': pygame.K_COMMA,
    ';': pygame.K_SEMICOLON, "'": pygame.K_QUOTE, '[': pygame.K_LEFTBRACKET,
    ']': pygame.K_RIGHTBRACKET,'-': pygame.K_MINUS,'/': pygame.K_SLASH,
    '\\': pygame.K_BACKSLASH, '=': pygame.K_EQUALS, '*': pygame.K_ASTERISK, '^': pygame.K_CARET,
}

#Sound
theme = pygame.mixer.Sound("music.mp3")
theme.play(-1)
click = pygame.mixer.Sound("click.mp3")
hover = pygame.mixer.Sound("hover.mp3")

#Menu button
expand = VideoFileClip("sprites/menu-expand.mp4")
collapse = VideoFileClip("sprites/menu-collapse.mp4")
play_button = pygame.image.load("sprites/play_button.png")
leave_button = pygame.image.load("sprites/leave_button.png")
settings_button = pygame.image.load("sprites/setting_button.png")
edit_button = pygame.image.load("sprites/edit_button.png")
setting_bar = pygame.image.load("sprites/Settings_side.png")
setting_bar_pos = [-550,0]

#Texts
title = pygame.font.Font("Assassin$.ttf",50)
text = pygame.font.Font("Type Machine.ttf",32)
text2 = pygame.font.Font("Type Machine.ttf",30)
text3 = pygame.font.Font("Type Machine.ttf", 25)
Lane1 = text.render("First Lane Key: ", True, "white")
Lane2 = text.render("Second Lane Key: ", True, "White") 
Lane3 = text.render ("Third Lane Key: ", True, "White")
Lane4=  text.render("Fourth Lane Key: ", True, "white")
mania_keys = title.render("Mania Keys ",True,'white')
osu_keys = title.render("Osu Keys", True,"white")
osu1 = text.render("First Key: ", True, "white")
osu2 = text.render("Second Key: " ,True, "white")
select = text3.render("Press any button", True, "white")

#Game
class Game:
    def __init__(self):
        

        #Display
        self.bg = pygame.image.load("sprites/background.png")
        self.in_menu = True
        self.icons = False
        self.inanimation = False
        self.playing = False
        self.editing = False
        self.frames = 0
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
        
        #Controls
        self.settinganim = False
        self.changekey = None
        self.changing = False
        
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
    
    def settings_animation(self, atype):
        if atype == "expand":
          while setting_bar_pos[0] != 0:
              pygame.display.update()
              setting_bar_pos[0] += 110
              screen.blit(setting_bar,(setting_bar_pos[0],setting_bar_pos[1]))
              pygame.display.update()
        else:
            while setting_bar_pos[0] != -550:
              pygame.display.update()
              setting_bar_pos[0] -= 110
              screen.blit(setting_bar,(setting_bar_pos[0],setting_bar_pos[1]))
              pygame.display.update()
        self.settinganim = False
            

    def update_key(self):
        keys = pygame.key.get_pressed()
        valid_keys = list(character_mapping.values())
        for key in valid_keys:
            if keys[key]:
                if key in [self.mkey1,self.mkey2,self.mkey3,self.mkey4,self.okey1,self.okey2]:
                    pass
                elif self.changekey == 0:
                    self.mkey1 = key
                elif self.changekey == 1:
                    self.mkey2 = key
                elif self.changekey == 2:
                    self.mkey3 = key
                elif self.changekey == 3:
                    self.mkey4 = key
                elif self.changekey == 4:
                    self.okey1 = key
                elif self.changekey == 5:
                    self.okey2 = key
                self.changekey = None
                self.changing = False


    def handle_settings(self):
        if setting_bar_pos[0] < 0 and not self.settinganim:
            self.settings_animation("expand")
            return
        if self.settinganim:
            return
        screen.blit(setting_bar,(setting_bar_pos[0],setting_bar_pos[1]))
        mouse = pygame.mouse.get_pos()
        position = [64,66]
        screen.blit(Lane1,(position[0],position[1]))
        screen.blit(Lane2,(position[0],position[1]+45))
        screen.blit(Lane3,(position[0],position[1]+45*2))
        screen.blit(Lane4,(position[0],position[1]+45*3))
        screen.blit(mania_keys, (59,8))
        screen.blit(osu_keys,(position[0],position[1]+45*4))
        screen.blit(osu1, (position[0],position[1]+50+45*4))
        screen.blit(osu2, (position[0],position[1]+50+45*5))

        pos = [355,70]
        for i in range(4):
            rect = pygame.Surface((220,32))
            rect.set_alpha(128)
            screen.blit(rect, (pos[0],pos[1]+45*i))
        for i in range(2):
            rect = pygame.Surface((220,32))
            rect.set_alpha(128)
            screen.blit(rect, (pos[0],pos[1]+50+ 45*(4+i)))

        l1_key = text2.render(pygame.key.name(self.mkey1).upper(),True,'white')
        l2_key = text2.render(pygame.key.name(self.mkey2).upper(),True,'white')
        l3_key = text2.render(pygame.key.name(self.mkey3).upper(),True,'white')
        l4_key = text2.render(pygame.key.name(self.mkey4).upper(),True,'white')
        o1_key = text2.render(pygame.key.name(self.okey1).upper(), True, 'white')
        o2_key = text2.render(pygame.key.name(self.okey2).upper(), True, 'white')



        if not (self.changekey == 0):
            screen.blit(l1_key, (pos[0]+100,pos[1]-3))
        else:
            screen.blit(select,(pos[0]+5,pos[1]-3))
        if not  (self.changekey == 1):
            screen.blit(l2_key, (pos[0]+100,pos[1]-3+45))
        else:
            screen.blit(select,(pos[0]+5,pos[1]-3+45))
        if not  (self.changekey == 2):
            screen.blit(l3_key, (pos[0]+100,pos[1]-3+45*2))
        else:
            screen.blit(select,(pos[0]+5,pos[1]-3+45*2))
        if not  (self.changekey == 3):
            screen.blit(l4_key, (pos[0]+100,pos[1]-3+45*3))
        else:
            screen.blit(select,(pos[0]+5,pos[1]-3+45*3))
        if not  (self.changekey == 4):
            screen.blit(o1_key, (pos[0]+100,pos[1]-3+50+45*4))
        else:
            screen.blit(select,(pos[0]+5,pos[1]-3+50+45*4))
        if not  (self.changekey == 5):
            screen.blit(o2_key, (pos[0]+100,pos[1]-3+50+45*5))
        else:
            screen.blit(select,(pos[0]+5,pos[1]-3+50+45*5))
        
        #Stops event if changing hotkey
        if self.changing:
            return
        
        if pygame.mouse.get_pressed()[0]:
            print(mouse)
            #Collapse Setting bar
            if 599 <= mouse[0]:
                self.settings_animation("collapse")
                self.controls = False

            #Detect key change
            if self.changekey == None:
                for i in range(4):
                    if pos[0] <= mouse[0] <= (pos[0]+220) and (pos[1]+45*i)<= mouse[1] <= ((pos[1]+45*i)+32):
                        self.changekey = i
                        self.changing = True
                for i in range(2):
                    if pos[0] <= mouse[0] <= (pos[0] + 220) and (pos[1]+45*(4+i)+50 <= mouse[1] <= pos[1]+45*(4+i)+50+32):
                        self.changekey = 4+i
                        self.changing = True
            
                
            


    def handle_menu_icons(self):
        mouse = pygame.mouse.get_pos()
        Play = True
        Edit = True
        Settings = True
        Leave = True

        #Resize Icon if Hover
        if not self.controls:
            if 631 <= mouse[0] <= 713 and 486<= mouse[1] <=604:
                screen.blit(pygame.transform.smoothscale(leave_button,(leave_button.get_width()+10,leave_button.get_height()+10)),(637, 477))
                hover.play() if not self.hoverplayed else None
                Leave = False
                self.hoverplayed = True
            elif 414 <= mouse[0] <= 533 and 312<= mouse[1] <= 412:
                screen.blit(pygame.transform.smoothscale(settings_button,(settings_button.get_width()+10,settings_button.get_height()+10)),(447, 301))
                hover.play() if not self.hoverplayed else None
                Settings = False
                self.hoverplayed = True
            elif  610 <= mouse[0] <=737 and 122 <= mouse[1] <= 212:
                screen.blit(pygame.transform.smoothscale(edit_button,(edit_button.get_width()+10,edit_button.get_height()+10)),(634, 113))
                hover.play() if not self.hoverplayed else None
                Edit = False
                self.hoverplayed = True
            elif 822 <= mouse[0] <= 917 and 312 <= mouse[1] <= 414:
                screen.blit(pygame.transform.smoothscale(play_button,(play_button.get_width()+10,play_button.get_height()+10)),(844, 301))
                hover.play() if not self.hoverplayed else None
                Play = False
                self.hoverplayed = True
            else:
                self.hoverplayed = False
        
        #Check for Resize and Display
        screen.blit(edit_button,(644, 123)) if Edit else None
        screen.blit(play_button, (844, 311)) if Play else None
        screen.blit(leave_button, (647, 487)) if Leave else None
        screen.blit(settings_button,(457, 311)) if Settings else None

        if pygame.mouse.get_pressed()[0] and not self.controls:
            if 631 <= mouse[0] <= 713 and 486<= mouse[1] <=604:
                click.play() if not self.clickplayed else None
                pygame.quit()
            elif 822 <= mouse[0] <= 917 and 312 <= mouse[1] <= 414:
                click.play() if not self.clickplayed else None
                self.in_menu = False
                self.icons = False
                theme.fadeout(1000)
                self.playing = True
            elif 414 <= mouse[0] <= 533 and 312<= mouse[1] <= 412:
                click.play() if not self.clickplayed else None
                self.controls = True
            
            


    def handle_animation(self, clip):
        fps = clip.fps
        delay = int(1000 / fps)  # Delay in milliseconds
        # Iterate through each frame
        for frame in clip.iter_frames():
            # Convert the frame to a pygame surfac 
            pygame_frame =  pygame.image.frombuffer(frame, frame.shape[1::-1], "RGB")
            screen.blit(pygame_frame, (0, 0))

            self.snowfall()
            pygame.display.flip()
            # Delay between each frame display
            pygame.time.delay(delay) 
            

    def menu_screen(self):

        if not self.inanimation:
            screen.blit(self.bg, (0,0))
        mouse = pygame.mouse.get_pos()
        expanding = False
        glow = False
        collapsing = False
        caxel_button = pygame.image.load("sprites/caxel_noglow.png")
        caxel_pos = [screen_width//2 - caxel_button.get_width()//2+8, screen_height//2 - caxel_button.get_height()//2-7]
        
        if self.icons:
            mcaxel_button = pygame.image.load('sprites\caxel_outline_opened.png')
            mcaxel_pos = [screen_width//2 - mcaxel_button.get_width()//2+2, screen_height//2 - mcaxel_button.get_height()//2-3]
            screen.blit(mcaxel_button, (mcaxel_pos[0], mcaxel_pos[1]))
            self.handle_menu_icons()
        else:
            if caxel_pos[0] < mouse[0] < caxel_pos[0] + caxel_button.get_width() and caxel_pos[1] < mouse[1] < caxel_pos[1] + caxel_button.get_height():
                caxel_button = pygame.image.load("sprites/caxel_glow.png")
                hover.play() if not self.hoverplayed else None
                glow = True
                self.hoverplayed = True
            else:
                self.hoverplayed = False
    
        
        if not (self.inanimation or self.icons):
                screen.blit(caxel_button, (caxel_pos[0], caxel_pos[1]))


        #Detect Mouse Press
        if pygame.mouse.get_pressed()[0] and not self.controls:
            caxel_button = pygame.image.load("sprites/caxel_noglow.png")
            caxel_pos = [screen_width//2 - caxel_button.get_width()//2+8, screen_height//2 - caxel_button.get_height()//2-7]
            
            #For Expanding Menu
            if caxel_pos[0] < mouse[0] < caxel_pos[0] + caxel_button.get_width() and caxel_pos[1] < mouse[1] < caxel_pos[1] + caxel_button.get_height():
                click.play() if not self.clickplayed else None
                
                if self.icons:
                    collapsing = True
                else:
                    expanding = True

                self.clickplayed = True
                if not self.inanimation:
                    self.inanimation = True
               
         
        if self.inanimation:
            if expanding:
               self.handle_animation(expand)
               self.icons = True
               expanding = False


            elif collapsing:
                self.handle_animation(collapse)
                self.icons = False
                collapsing = False
                
            self.inanimation = False
            self.clickplayed = False
            
            
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

    def update(self):

        if self.changing:
            self.update_key()


        if self.in_menu:
            self.menu_screen()
            self.snowfall()
        if self.playing:
            self.gameplay()
        if self.controls:
            self.handle_settings()
      

game = Game()

#Game Code
while in_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    game.update()
    pygame.display.update()
    clock.tick(60)
