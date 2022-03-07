import state_machine, classes
import pygame as pg
from constants import *

class Gameplay(state_machine.GameState):

    def __init__(self):
        super(Gameplay,self).__init__()

    def startup(self, persistent):
        super().startup(persistent)
        self.user_name = self.persist["username"]
        self.board = classes.Board()
        self.counter = 0
        self.pause = False

    
    def get_events(self,events):
        for event in events:
            if event.type == pg.QUIT:
                self.quit = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    self.pause = not self.pause
                if event.key == pg.K_SPACE:
                    self.board.reset()
                if self.pause:
                    return
                if event.key == pg.K_UP:
                    self.board.active_block.rotate()
                if event.key == pg.K_RIGHT:
                    self.board.active_block.move_right()
                if event.key == pg.K_LEFT:
                    self.board.active_block.move_left()
                if event.key == pg.K_DOWN:
                    self.board.active_block.move_down()

    def update(self, dt):
        if self.pause:
            return

        self.counter+=1
        if self.counter>10000:
            self.counter = 0
        
        if self.board.active_block is not None:
            if self.counter % 20 == 0: 
                self.board.active_block.move_down()
        
        if self.board.active_block == None:
            print("NEW BLOCK CREATED")
            self.board.active_block = classes.Block(6, 0, self.board)
            if self.board.active_block.intersects():
                self.board.reset()

        if self.board.active_block is not None:
            keys = pg.key.get_pressed()
            if keys[pg.K_DOWN] and self.counter % 3 == 0:
                self.board.active_block.move_down()

    def draw(self, surface):
        #rendering black screen
        surface.fill(BLACK)

        #rendering board
        for i in range(BOARD_HEIGHT):
            for j in range(BOARD_WIDTH):
                #rendering empty board
                pg.draw.rect(surface,WHITE,[x0+BOARD_SIDE*j,y0+BOARD_SIDE*i,BOARD_SIDE, BOARD_SIDE],1)
                #rendering colors
                if self.board.color[i][j]>0:
                    pg.draw.rect(surface,classes.colors[self.board.color[i][j]],[x0+BOARD_SIDE*j+1,y0+BOARD_SIDE*i+1,BOARD_SIDE-2, BOARD_SIDE-2])
      
        #rendering current active block
        if self.board.active_block is not None:
            for x in self.board.active_block.image():
                i = x // 4
                j = x % 4
                pg.draw.rect(surface,classes.colors[self.board.active_block.col],[x0+BOARD_SIDE*(self.board.active_block.x+j),y0+BOARD_SIDE*(self.board.active_block.y+i),BOARD_SIDE-2, BOARD_SIDE-2])

        #rendering current score
        font = pg.font.SysFont('Calibri', 25, True, False)
        text = font.render("Score: "+str(self.board.score),True,WHITE)
        surface.blit(text,(0,0))
        if self.pause:
            pause_text = font.render("Game paused!",True,WHITE)
            surface.blit(pause_text,(self.screen_rect.centerx-(pause_text.get_width()/2),0))
