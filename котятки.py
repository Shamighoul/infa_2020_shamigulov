import pygame
from pygame.draw import *

global grey
global brown
global green
global floor
global gay
global ugh
global wall
global blue
global black

pygame.init()

FPS = 30
height = 560
width = 395
#colors
brown = (186, 134, 37)
floor = (100, 40, 0)
wall = (165, 42, 42)
blue = (0, 0, 255)
gay = (127, 255, 212)
black = (0, 0, 0)
grey = (43, 43, 43)
green = (255,100,180)
ugh = (0,255,170)

screen = pygame.display.set_mode((width, height))

rect(screen, wall, (0,0, width, height//2))
def draw_windows(s, w, h, c):
    '''
    s - рисует на плоскости(скрине)
    w - ширина окна
    h - высота картины
    с - количество окон на стене
    '''
    b=1
    for i in range(c):
        rect(s, gay, (b,11, w, 1.34*w))
        a=b+10
        for i in range(2):
            rect(s, blue, (a, 0.15*w, 0.4*w, 0.31*w))
            rect(s, blue, (a, 0.515*w, 0.4*w, 0.806*w))
            a+=0.45*w
        b+=1.34*w

#рисуем низ
rect(screen, floor, (0, 255, 396, 305))
#make ball
def ball(s, x, y, r):
    '''
    s - рисует на плоскости(скрине)
    х - координаты по х
    у - координата по у
    r - радиус мяча
    '''
    line(s, black, (x-1.6*r, y+0.6*r), (x+0.6*r, y+0.6*r), 1)
    circle(s, grey, (x, y), r)
    b=y-0.6*r
    for i in range(3):
        line(s,black,(x-0.6*r,b),(x+0.6*r,2*y-b),1)
        b+=r/6

        
        
#рисуем большого cat
def cat(x,y,l,w,z1,d1,t, x1):
    '''
    x - координаты на плоскости
    y - координаты по у на скрине и плоскости
    l - длина кота
    w - ширина кота
    z1- 1(отражение по х) 0(бездействие)
    d1- 1(отражение по у) 0(бездействие)
    t - T(серого цвета) or F(оранжевый)
    x1 - координаты относительно центра скрина по х
    '''
    big=pygame.Surface((width, height))
    big.set_colorkey(black)
    if t:
        color = (180, 180, 180)
    else:
        color = brown
    
    ellipse(big,color,(250,300,150,60))
    ellipse(big,black,(250,300,150,60),1)

    ellipse(big,color,(50,265,260,140))
    ellipse(big,black,(50,265,260,140),1)

    ellipse(big,color,(34,330,31,50))
    ellipse(big,black,(34,330,31,50),1)

    ellipse(big,color,(56,370,74,40))
    ellipse(big, black,(56,370,74,40),1)

    ellipse(big,color,(10,275,100,90))
    ellipse(big,black,(10,275,100,90),1)


    circle(big, color, (270,370), 45)
    circle(big, black, (270,370), 45,1)

    ellipse(big,color,(280,380,35,65))
    ellipse(big,black,(280,380,35,65),1)

    #ears and eyes
    polygon(big, color, [(85,285), (110,270),
                                   (105,305)])
    polygon(big, black, [(85,285), (110,270),
                                   (105,305)],1)
    polygon(big, green, [(90,285), (105,275),
                                   (105,300)])
    polygon(big, black, [(90,285), (105,275),
                                   (105,300)],1)

    polygon(big, color, [(8,273), (17,305),
                                   (35,287)])
    polygon(big, black, [(8,273), (17,305),
                                   (35,287)],1)
    polygon(big, green, [(11,278), (18,300),
                                   (30,286)])
    polygon(big, black, [(11,278), (18,300),
                                   (30,286)],1)
    x=34
    for i in range(2):
        ellipse(big, ugh, (x,305,20,25))
        ellipse(big, black, (x,305,20,25), 1)
        ellipse(big, black, (x+10, 306, 5, 20), 0)
        x+=46
    polygon(big, green, [(61,340), (69,340),
                                   (65,345)])
    polygon(big, black, [(61,340), (69,340),
                                   (65,345)],1)
    line(big,black,(65,345),(65,350),1)

    #moustache
    line(big,black,(75,345),(120,340),1)
    line(big,black,(75,348),(120,348),1)
    line(big,black,(75,351),(120,356),1)
    line(big,black,(55,345),(30,340),1)
    line(big,black,(55,348),(30,348),1)
    line(big,black,(55,351),(30,356),1)
    big=pygame.transform.smoothscale(big,(l,w))
    big=pygame.transform.flip(big,z1,d1)
    screen.blit(big,(x1,y))
    
    
    
ball(screen, 240, 500, 30)
ball(screen, 70,400,20)
ball(screen, 300,370,20)    
        
cat(0,350,120,280,1,0, True,100 )
cat(0,200,150,250,1,0, True, 160)
cat(0,140,180,280,0,0, False, -20)
cat(0,250,150,250,0,0, False, 100)

draw_windows(screen, 84, height, 4)




pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
