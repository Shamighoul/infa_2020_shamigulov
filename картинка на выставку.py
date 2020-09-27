import pygame
from pygame.draw import *
import numpy as n

pygame.init()

screen = pygame.display.set_mode((397, 561))

rect(screen, (255, 255, 255), (0, 280, 397, 561))
#cat's paws
s = pygame.Surface((200, 1000))
rect(s, (255, 255, 255), (0, 0, 200, 1000))
ellipse(s, (200, 200, 200), (5,5, 50, 14))
ellipse(s, (200, 200, 200), (80,45, 14, 50))
ellipse(s, (200, 200, 200), (65,35, 14, 50))
ellipse(s, (200, 200, 200), (80,35, 60, 14))
s = pygame.transform.rotate(s, 45)
screen.blit(s, (50,300))
#human's right hand
s = pygame.Surface((397, 1000))
rect(s, (255, 255, 255), (0, 0, 397, 561))
ellipse(s, (200, 200, 50), (0,0, 20, 40))
a = pygame.transform.rotate(s, 60)
screen.blit(a, (355, 50))

rect(screen, (210, 210, 210), (0, 0, 397, 280))

pygame.display.update()

#igly
s = pygame.Surface((220, 140))
rect(s, (210, 210, 210), (0, 0, 220, 60))
rect(s, (255, 255, 255), (0, 60, 397, 140))
ellipse(s, (200, 200, 200), (0, 0, 220, 280))
arc(s, (0, 0, 0), (0, 0, 220, 280), 4, n.pi)
line(s, (0,0,0), [0, 138], [220, 138])
line(s, (0,0,0), [6, 105], [214, 105])
line(s, (0,0,0), [15, 70], [205, 70])
line(s, (0,0,0), [35, 35], [185, 35])
x1 = 0; y1 = 105
x2 = 220; y2 = 138
N = 5
h = (x2 - x1) // (N + 1)
x = x1 + h
for i in range(N):
    line(s, (0,0,0), (x, y1), (x, y2))
    x += h
x1 = 15; y1 = 70
x2 = 205; y2 = 105
N = 4
h = (x2 - x1) // (N + 1)
x = x1 + h
for i in range(N):
    line(s, (0,0,0), (x, y1), (x, y2))
    x += h
x1 = 35; y1 = 70
x2 = 185; y2 = 35
N = 3
h = (x2 - x1) // (N + 1)
x = x1 + h
for i in range(N):
    line(s, (0,0,0), (x, y1), (x, y2))
    x += h
x1 = 35; y1 = 5
x2 = 185; y2 = 35
N = 2
h = (x2 - x1) // (N + 1)
x = x1 + h
for i in range(N):
    line(s, (0,0,0), (x, y1), (x, y2))
    x += h
screen.blit(s, (30,220))

pygame.display.update()

#human
ellipse(screen, (200, 200, 50), (305,350, 80, 200))
rect(screen, (255, 255, 255), (290, 440, 320, 420))
circle(screen, (200,200,200), (345,350), 30)
circle(screen, (230,230,230), (345,350), 25)
line(screen, (0,0,0), [330, 335], [340, 340])
line(screen, (0,0,0), [360, 335], [350, 340])
arc(screen, (0, 0, 0), (335, 355, 20, 20), 0, n.pi)
ellipse(screen, (200, 200, 50), (280,370, 40, 20))
line(screen, (0,0,0), [290, 335], [290, 460])
    
ellipse(screen, (200, 200, 50), (355,420, 20, 40))
ellipse(screen, (200, 200, 50), (315,420, 20, 40))
ellipse(screen, (200, 200, 50), (355,450, 30, 10))
ellipse(screen, (200, 200, 50), (300,450, 30, 10))

rect(screen, (48, 41, 37), (305, 430, 80, 10))
rect(screen, (48, 41, 37), (340, 380, 10, 60))

pygame.display.update()

#cat
ellipse(screen, (200, 200, 200), (73,405, 80, 28))
ellipse(screen, (200, 200, 200), (48,419, 40, 14))
ellipse(screen, (200, 200, 200), (65,383, 35, 28))
polygon(screen, (200,200,200), [(83,383), (89,385),
                               (86,378)])
polygon(screen, (200,200,200), [(92,387), (98,390),
                               (94,380)])
polygon(screen, (0,0,0), [(74,398), (76,398),
                               (75,400)])

#fish
ellipse(screen, (20,255,210), (65,405, 25,10))
polygon(screen, (20,255,210), [(90,410),(95,405),(95,415)])

polygon(screen, (255, 255, 255), [(73,406), (77,405),
                               (75,408)])
polygon(screen, (255, 255, 255), [(77,406), (82,406),
                               (80,408)])
                               
#cat's eyes
ellipse(screen, (255, 255, 255), (70,390, 7, 6))
ellipse(screen, (255, 255, 255), (81,392, 7, 6))
ellipse(screen, (0, 0, 0), (75,392, 2, 2))
ellipse(screen, (0, 0, 0), (86,394, 2, 2))

pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
