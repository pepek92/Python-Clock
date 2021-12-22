import pygame
import math
from datetime import datetime
 
pygame.init()
white = (255, 255, 255)
width, height = 720, 560
screen = pygame.display.set_mode((width, height))
 
def circle(color: int, radius: int):
    pygame.draw.circle(screen, color, (middle_x, middle_y), radius)
 
def pointer(length: int, thickn: int, share: float):
    angle = 2*math.pi*share-math.pi/2
    end_x = middle_x+math.cos(angle)*length
    end_y = middle_y+math.sin(angle)*length
 
    pygame.draw.line(screen, (255, 255, 255), (middle_x, middle_y), (end_x, end_y), thickn)
 
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
 
    hours = datetime.now().hour%12
    minutes = datetime.now().minute
    seconds = datetime.now().second
 
    pygame.display.set_caption(str(datetime.now().time())[:8])
 
    screen.fill((0, 0, 0))
 
    middle_x = width/2
    middle_y = height/2
 
    circle((255, 0, 0), 220)
    circle((0, 0, 0), 210)
    
    pointer(205, 1, seconds/60)
    pointer(195, 3, (minutes+seconds/60)/60)
    pointer(165, 6, (hours+minutes/60+seconds/3600)/12)
    circle((0, 0, 0), 20)
 
    pygame.display.flip()