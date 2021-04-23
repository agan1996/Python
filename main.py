import pygame
import random

class Point:
    row=0
    col=0
    def __init__(self,row,col):
        self.row=row
        self.col=col
    def copy(self):
        return Point(row=self.row,col=self.col,)

pygame.init()
W=800
H=600
ROW=30
COL=40
size=(W,H)
window=pygame.display.set_mode(size)
pygame.display.set_caption('SNAKEE')

bg_color=(230,230,220)
snake_color=(128,128,128)


head=Point(row=int(ROW/2),col=int(COL/2))
head_color=(200,100,80)

snakes=[
    Point(row=head.row,col=head.col+1),
    Point(row=head.row,col=head.col+2),
    Point(row=head.row,col=head.col+3),
    Point(row=head.row, col=head.col + 4),
    Point(row=head.row, col=head.col + 5),
    Point(row=head.row, col=head.col + 6)
]

food=Point(row=random.randint(0,ROW-1),col=random.randint(0,COL-1))
def gen_food():
    while 1:
        pos=Point(row=random.randint(0,ROW-1),col=random.randint(0,COL-1))
        is_collap=False
        if head.row==pos.row and head.col==pos.col:
            is_collap=True
        for snake in snakes:
            if snake.row==food.row and snake.col== food.col:
                break
        if not  is_collap:
            break
    return pos

food=gen_food()   #
food_color=(255,255,0)

def rect(point,color):
  cell_width=W/COL
  cell_height=H/ROW
  left=point.col*cell_width
  top=point.row*cell_height
  pygame.draw.rect(window,color,(left,top,cell_width,cell_height))
  pass

#游戏循环--------------------------------------------
quit = False
clock=pygame.time.Clock()
direct='left'

while not quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit=True

        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                direct='up'
            elif event.key==pygame.K_DOWN:
                direct='down'
            elif event.key==pygame.K_LEFT:
                direct='left'
            elif event.key==pygame.K_RIGHT:
                direct='right'

                # eat
    eat = (head.row == food.row and head.col == food.col)
    snakes.insert(0,head.copy())
    if not eat:
        snakes.pop()
    elif eat :
        food = gen_food()#


    #移动
    if direct=='left':
        head.col-=1
    elif direct=='right':
        head.col+=1
    elif direct=='up':
        head.row-=1
    elif direct=='down':
        head.row+=1
    #撞墙
    dead = False
    if head.col<0 or head.col>COL or head.row<0 or head.col>COL:
        dead = True
    for snake in snakes:
        if head.col == snake.col and head.row == snake.row:
            dead=True
            break
    if dead:
        print('GAME OVER!!')
       # window = pygame.display  ??
        quit=True

    #撞自己

    #渲染
    pygame.draw.rect(window,bg_color,(0,0,W,H))
    #蛇头
    rect(head,head_color)
    rect(food,food_color)
    #画蛇
    for snake in snakes:
        rect(snake,snake_color)
    pygame.display.flip() # 让出控制权给系统
    clock.tick(10)

