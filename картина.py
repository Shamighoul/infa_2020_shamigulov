import pygame
from pygame.draw import *
import numpy as n
global sky
global white
global black
global grey
global face_cl
global brown
global closer
global blue 

pygame.init()

sky = (220, 220, 220)
grey = (200, 200, 200)
closer = (200, 200, 50)
brown = (48, 41, 37)
black = (0,0,0)
face_cl = (230, 230, 230)
white = (255,255,255)
br = (45, 37, 220)
blue = (20,255,210)

height = 561
width = 397
screen = pygame.display.set_mode((width, height))
s = pygame.Surface((width, height))
s.fill(br)
s.set_colorkey(br)

rect(screen, white , (0, height//3, width, height))
rect(screen, sky , (0, 0, width, height//3))

def cat_fish(s, x, y, w):
    #cat's paws
    a = pygame.Surface((width, height))
    a.fill(br)
    a.set_colorkey(br)
    ellipse(a, grey, (5,5, 5*w//8, 7*w//40))
    ellipse(a, grey, (5+75*w//80,5+40*w//80, 7*w//40, 5*w//8))
    ellipse(a, grey, (5+60*w//80,5+30*w//80, 7*w//40, 5*w//8))
    ellipse(a, grey, (5+75*w//80,5+30*w//80, 6*w//8, 7*w//40))
    a = pygame.transform.rotate(a, 45)
    s.blit(a, (-6-w//5+x, -306.2 + 105.6*w/80-22.2*((w/80)**2)
               -35.8*((w/80)**3)+15.9*((w/80)**4)+y))
    #cat 73 405 80
    ellipse(s, grey, (x,y, w, 7*w//20))
    ellipse(s, grey, (x-5*w//16,y+3*w//20, w//2, 7*w//40))
    ellipse(s, grey, (x-w//10,y-11*w/39, 7*w//16, w*7//20))
    polygon(s, grey, [(x+w//40,y-w/4), (x+7*w//40,y-w//4),
                               (x+3*w//20,y-27*w//80)])
    polygon(s, grey, [(x+13*w//80,y-9*w//39), (x+5*w//16,y-3*w//16),
                               (x+21*w//79,y-5*w//16)])
    polygon(s, black, [(x+w//79,y-7*w//79), (x+3*w//79,y-7*w//79),
                               (x+w//40,y-w//16)])

    #fish
    ellipse(s, blue, (x-w//10,y, w//3,w//8))
    polygon(s, blue, [(x+17*w//79,y+w//16),(x+22*w//79,y),(x+22*w//79,y+w//8)])

    polygon(s, white, [(x,y+w//79), (x+w//20,y),
                               (x+w//39,y+3*w//79)])
    polygon(s, white, [(x+w//20,y+w//79), (x+9*w//79,y+w//79),
                               (x+7*w//79,y+3*w//79)])


    #cat's eyes
    ellipse(s, white, (x-3*w//79,y-3*w//16, w//11, w//13))
    ellipse(s, white, (x+w//10,y-11*w//79, w//11, w//13))
    ellipse(s, black, (x+w//39,y-11*w//79, w//40, w//40))
    ellipse(s, black, (x+13*w//79,y-9*w//79, w//40, w//40))
    
    screen.blit(s, (0,0))
    
def draw_igly(s, x, y, w, h):
    ellipse(s, grey, (x, y, w, h*2))
    arc(s, black, (x, y, w, h*2), 4, n.pi)
    x1 = x; y1 = y+h*0.75
    x2 = w+x; y2 = y+h*69/70
    line(s, black, [x1, y2], [x2, y2])
    N = 5
    hx = (x2 - x1) // (N + 1)
    xx = x1 + hx
    for i in range(N):
        line(s, black, (xx, y1), (xx, y2))
        xx += hx
    x1 = 6/220*w+x; y1 = y+h*0.5
    x2 = x+w-6/220*w; y2 = y+h*0.75
    line(s, black, [x1, y2], [x2, y2])
    N = 4
    hx = (x2 - x1) // (N + 1)
    xx = x1 + hx
    for i in range(N):
        line(s, black, (xx, y1), (xx, y2))
        xx += hx
    x1 = 15/220*w+x; y1 = y+h*0.5
    x2 = x+w-15/220*w; y2 = y+h*0.25
    line(s, black, [x1, y1], [x2, y1])
    N = 3
    hx = (x2 - x1) // (N + 1)
    xx = x1 + hx
    for i in range(N):
        line(s, black, (xx, y1), (xx, y2))
        xx += hx
    x1 = 35/220*w+x; y1 = y+h*0.25
    x2 = x+w-35/220*w; y2 = y+h/28
    line(s, black, [x1, y1], [x2, y1])
    N = 2
    hx = (x2 - x1) // (N + 1)
    xx = x1 + hx
    for i in range(N):
        line(s, black, (xx, y1), (xx, y2))
        xx += hx
    rect(s, white, (x,y+h, w, h))
    screen.blit(s,(0,0))

def draw_human(s, x, y, w, l):
    #human's right hand
    #w=80
    if l:
        ellipse(s, closer, (x+10*w//16,y+w//4, w//2, w//4))
        line(s, black, [x-w*3//16, y-w*3//16], [x-w*3//16, y+w*11//8])
        ellipse(s, closer, (x-5*w//16,y+w//4, w//2, w//4))
    else:
        ellipse(s, closer, (x-4*w//16,y+w//4, w//2, w//4))
        line(s, black, [x+w*17//16, y-w*3//16], [x+w*17//16, y+w*11//8])
        ellipse(s, closer, (x+11*w//16,y+w//4, w//2, w//4))
    #305=x   350=y
    ellipse(s, closer, (x,y, w, 2.5*w))
    rect(s, white, (x-w*3//16, y+w*9//8, w*1.2, 1.25*w*1.2))
    circle(s, grey, (x+w//2, y), 3*w//8)
    circle(s, face_cl, (x+w//2,y), 5*w//16)
    line(s, black, [x+5*w//16, y-3*w//16], [x+7*w//16, y-w//8])
    line(s, black, [x+11*w//16, y-3*w//16], [x+9*w//16, y-w//8])
    arc(s, black, (x+3*w//8, y+w//16, w//4 , w//4), 0, n.pi)
    
    ellipse(s, closer, (x+5*w//8,y+7*w//8, w//4, w//2))
    ellipse(s, closer, (x+w//8,y+7*w//8, w//4, w//2))
    ellipse(s, closer, (x+5*w//8,y+5*w//4, w*3//8, w//8))
    ellipse(s, closer, (x-w//16,y+5*w//4, w//8*3, w//8))

    rect(s, brown, (x, y+w, w, w//8))
    rect(s, brown, (x+7*w//16, y+w//8*3, w//8, w*0.75))
    screen.blit(s,(0,0))
    
#iglies
draw_igly(s,-20,150,80,51)
draw_igly(s,170,160,80,51)
draw_igly(s,100,165,95,60.5)
draw_igly(s,10,180,110,70)
draw_igly(s,90,200,165,105)
draw_igly(s,-30,220,220,140)

#humans
draw_human(s, 300, 180, 24, False)
draw_human(s, 320, 200, 28, True)
draw_human(s, 350, 220, 32, False)
draw_human(s, 260, 220, 32, False)
draw_human(s, 330, 230, 34, False)
draw_human(s, 280, 230, 38, True)
draw_human(s, 280, 230, 38, True)
draw_human(s, 220, 270, 48, True)
draw_human(s, 330, 280, 53, False)
draw_human(s, 305, 350, 78, True)
    
#cats
cat_fish(screen, 350, 490, 80)    
cat_fish(screen, 11, 380, 40) 
cat_fish(screen, -22, 420, 40) 
cat_fish(screen, 102, 410, 60) 
cat_fish(screen, 22, 460, 40) 
cat_fish(screen, 282, 550, 60) 
cat_fish(screen, 122, 490, 40)
cat_fish(screen, 2, 520, 60) 
cat_fish(screen, 220, 390, 40) 
cat_fish(screen, 242, 450, 60) 
cat_fish(screen, 182, 530, 40) 

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
