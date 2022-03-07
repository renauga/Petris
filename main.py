import pygame as pg 
import classes
from constants import *

if __name__ == "__main__":
    pg.init()

    screen = pg.display.set_mode((800,900))

    board = classes.Board()

    running = True

    counter = 0

    while running:


        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    board.reset()
                if event.key == pg.K_UP:
                    board.active_block.rotate(board)
                if event.key == pg.K_RIGHT:
                    board.active_block.move_right(board)
                if event.key == pg.K_LEFT:
                    board.active_block.move_left(board)
                if event.key == pg.K_DOWN:
                    board.active_block.move_down(board)

        counter+=1
        if counter>100000:
            counter = 0

        if board.active_block is not None:
            if counter % 100 == 0: 
                board.active_block.move_down(board)
        
        if board.active_block == None:
            print("NEW BLOCK CREATED")
            board.active_block = classes.Block(6, 0)
            if board.active_block.intersects(board):
                board.reset()

        if board.active_block is not None:
            keys = pg.key.get_pressed()
            if keys[pg.K_DOWN] and counter % 25 == 0: 
                board.active_block.move_down(board)
        
        #rendering black screen
        screen.fill(BLACK)

        #rendering board
        for i in range(BOARD_HEIGHT):
            for j in range(BOARD_WIDTH):
                #rendering empty board
                pg.draw.rect(screen,WHITE,[x0+BOARD_SIDE*j,y0+BOARD_SIDE*i,BOARD_SIDE, BOARD_SIDE],1)
                #rendering colors
                if board.color[i][j]>0:
                    pg.draw.rect(screen,classes.colors[board.color[i][j]],[x0+BOARD_SIDE*j+1,y0+BOARD_SIDE*i+1,BOARD_SIDE-2, BOARD_SIDE-2])

                
        #rendering current active block
        if board.active_block is not None:
            for x in board.active_block.image():
                i = x // 4
                j = x % 4
                pg.draw.rect(screen,classes.colors[board.active_block.col],[x0+BOARD_SIDE*(board.active_block.x+j),y0+BOARD_SIDE*(board.active_block.y+i),BOARD_SIDE-2, BOARD_SIDE-2])


        #rendering current score
        text = pg.font.SysFont('Calibri', 25, True, False).render("Score: "+str(board.score),True,WHITE)
        screen.blit(text,(0,0))

        pg.display.update()


    pg.quit()