import pygame
from pygame.draw import *
from random import randint
import os.path
pygame.init()



FPS = 5
n=2
n1=1
hgt = 700
ln = 900
screen = pygame.display.set_mode((ln, hgt))
#задаем цвета кругов
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
# и массивы для множества шаров            
x = [0 for i in range(5+n1)]
y = [0 for i in range(5+n1)]
r = [0 for i in range(5+n1)]
a = [0 for i in range(5+n1)]
color = [0 for i in range(5+n1)]
x_change = [0 for j in range(5+n1)]
y_change = [0 for j in range(5+n1)]
boss_runx = 0
boss_runy = 0
global boss_runx, boss_runx 

def cor():
    '''
    функция задает изменеие направления движения круга из-за столкновния 
    x_change[g] - изменение по Х оси
    у_change[g] - изменение по У оси
    х[g] - координата х шара g
    y[g] - координата у шара g
    r[g] - радиус шара g
    distation - дистанция между шарами
    
    '''
    for g in range(n):
        if (x[g]+r[g]) >= ln-10  or (x[g]-r[g])<=0:
            x_change[g] =0-x_change[g]
        elif (y[g]+r[g])>=hgt-10 or (y[g]-r[g]) <=0:
            y_change[g] = 0-y_change[g]
        for d in range(n):
            distation=(x[g]-x[d])**2+(y[d]-y[g])**2
            if distation <=(r[d]+r[g])**2 and d!=0:
                y_change[d], y_change[g] = y_change[g], y_change[d]
                x_change[d], x_change[g] = x_change[g], x_change[d] 
                

def move():
    '''
    функция задает изменеие координаты круга, стирая и рисую круги снова после изменения параметра их координат 
    x_change[g] - изменение по Х оси
    у_change[g] - изменение по У оси
    х[g] - координата х шара g
    y[g] - координата у шара g
    r[g] - радиус шара g
    
    '''
    for i in range(n):
        x_change[i] = randint(-15, 15)
        y_change[i] = randint(-15, 15)
    for j in range(30):
        clock.tick(15)
        pygame.display.update()
        screen.fill(BLACK)
        for i in range(n):
            x[i] += x_change[i]
            y[i] += y_change[i]
            circle(screen, color[i], (x[i], y[i]), r[i])
        cor()    
          
def move_boss():
    '''
    успей нанести 10 дамага боссу пока он не сбежал
    '''
    boss_runx = 0
    boss_runy = 0
    for i in range(5):
        clock.tick(10)
        boss_runx += 100
        boss_runy += 100
        screen.fill(BLACK)
        rect(screen, COLORS[randint(0,5)], (boss_runx, boss_runy, ln - 2*boss_runx , hgt - 2*boss_runy))
        pygame.display.update()
    
def new_balls():
    '''рисует новый шарик
    с параметрами 
    х[g] - координата х шара g
    y[g] - координата у шара g
    r[g] - радиус шара g
    '''
    for i in range(n):
        x[i] = randint(100, ln -100)
        y[i] = randint(100, hgt - 100)
        r[i] = randint(30, 100)
        color[i] = COLORS[randint(0, 5)]
        circle(screen, color[i], (x[i], y[i]), r[i])
    move()
    
def boss():
    '''
    появился повелитель этажа
    '''
    rect(screen, COLORS[randint(0,5)], (0, 0, ln, hgt))
    pygame.display.update()
    move_boss()
    bmode = False

def click(event):
    '''
    функция вызываемая при нажатии на ЛКМ 
    определяет попали ли мы в цель и дает нам за это очки и уровни
    при повышении уровня количество целей за цикл увеличивается
    '''
    global n, combo, goal
    if combo>=10*n:
        n+=1
        combo=0
    if ball_num>=n*5 and goal>=3*n:
        if boss_runx<event.pos[0]<(ln - 2*boss_runx) and boss_runy<event.pos[1]<(hgt - 2*boss_runy):
            combo += 1
            print("damage")
    else:
        for i in range(n):
            a[i]=(event.pos[0]-x[i])**2+(event.pos[1]-y[i])**2
            for j in range(n):
                if a[i]<=(r[j]**2):
                    print('мяч пойман')
                    goal += 1   
                    x[i] = 0
                    y[i] = 0
                    r[i] = 0
                    color[i] = COLORS[0]
    
    
    

pygame.display.update()
clock = pygame.time.Clock()
finished = False



#игровой момент
'''
начало игры 1 уровень, 0 очков, игра началась 
'''
combo = 0
goal = 0
ball_num = 0
while not finished:
    clock.tick(FPS)
    if ball_num>=n*5 and goal>=3*n:
        boss()
    else:
        new_balls()
        ball_num += n
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                click(event)
        elif goal<=ball_num-7*n:
            finished = True
            
        screen.fill(BLACK)
    print(str(goal) + "from: " + str(ball_num))





pygame.quit()
goal += (n-2)*5
print(str(goal) + " from: " + str(ball_num))

'''
игра завершена следущие строчки сравнивают результат турнирной таблицы с результатом игрока и определят его место в таблице
'''
name = input()
if not os.path.exists('table.txt'):
    out = open('table.txt', 'tw', encoding='utf-8')
else:
    inp = open('table.txt', 'r')
    data = inp.readlines()
    inp.close()
    out = open('table.txt', 'w' )
n = len(data)
for i in range(n):
    s = list(data[i].split())
    if(int(s[1])<=goal):
        data[i]=('\n' + data[i])
        data.insert(i,(name +" " + str(goal)))
        break
for i in range(data.count('')):
    data.remove('')
if n==len(data):
    data.append('\n' + name + str(goal))
for i in range(len(data)):
    out.write(str(data[i]))
out.close()
