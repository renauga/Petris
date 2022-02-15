import math
from random import randint, random
import pygame, classes

pygame.init()

screen = pygame.display.set_mode((800,900))
WHITE = (255,255,255)
GRAY = (127,127,127)
BLACK = (0,0,0)

x0 = 100
y0 = 50

board = classes.Game(20,15,40)


running = True

pressing_down = False

counter = 0 
while running:
    counter+=1
    if counter>100000:
        counter = 0
    
    if board.active_block == None:
        print("NEW BLOCK CREATED")
        board.active_block = classes.Block(6, 0)
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                board.reset()
            if event.key == pygame.K_UP:
                board.active_block.rotate()
            if event.key == pygame.K_RIGHT:
                board.active_block.move_right()
            if event.key == pygame.K_LEFT:
                board.active_block.move_left()
            if event.key == pygame.K_DOWN:
                pressing_down = True
                board.active_block.move_down()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pressing_down = False


    if board.active_block is not None:
        if counter % 100 == 0: 
            board.active_block.move_down()
        if pressing_down and counter % 25 == 0: 
            board.active_block.move_down()
    
    #rendering black screen
    screen.fill(BLACK)

    #rendering board
    for i in range(board.height):
        for j in range(board.width):
            #rendering empty board
            pygame.draw.rect(screen,WHITE,[x0+board.side*j,y0+board.side*i,board.side, board.side],1)
            #rendering colors
            if board.color[i][j]>0:
               pygame.draw.rect(screen,classes.colors[board.color[i][j]],[x0+board.side*j+1,y0+board.side*i+1,board.side-2, board.side-2])

            
    #rendering current active block
    if board.active_block is not None:
        for x in board.active_block.image():
            i = math.floor(x/4)
            j = x%4
            pygame.draw.rect(screen,classes.colors[board.active_block.col],[x0+board.side*(board.active_block.x+j),y0+board.side*(board.active_block.y+i),board.side-2, board.side-2])

    pygame.display.update()


pygame.quit()