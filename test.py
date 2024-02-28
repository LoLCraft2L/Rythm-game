 
import pygame
import random
pygame.init()
 
WHITE = [255, 255, 255]
GREEN  = [0,255,0]
SIZE = [400, 400]
 
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Programming World of GFG")
 
snowFall = []
for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snowFall.append([x, y])
 
clock = pygame.time.Clock()
done = False
while not done:
 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True
    screen.fill(WHITE)
    for i in range(len(snowFall)):
        pygame.draw.circle(screen, GREEN, snowFall[i], 2)
 
        snowFall[i][1] += 0.3
        if snowFall[i][1] > 400:
            y = random.randrange(-50, -10)
            snowFall[i][1] = y
        
            x = random.randrange(0, 400)
            snowFall[i][0] = x
 
    pygame.display.flip()
    clock.tick(60)
pygame.quit()