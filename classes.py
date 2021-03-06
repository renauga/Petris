import random
from typing import List
from constants import BOARD_HEIGHT, BOARD_WIDTH, colors


class Board:
    def __init__(self):
        self.color = [[0]*BOARD_WIDTH for i in range(BOARD_HEIGHT)]
        self.score = 0
        self.active_block = Block(6,0,self)

    def reset(self):
        print("BOARD RESET")
        self.__init__()

    def freeze(self):
        for p in self.active_block.image():
            x = self.active_block.x + p % 4
            y = self.active_block.y + p // 4
            self.color[y][x] = self.active_block.col
        self.active_block = None
        self.line_destruct()

    def line_destruct(self):
        lines_destroyed = 0
        stk = []
        for i in range(BOARD_HEIGHT):
            all_filled = True
            line = List.copy(self.color[i])
            for j in range(BOARD_WIDTH):
                if self.color[i][j]==0:
                    all_filled=False
                self.color[i][j]=0
            if all_filled:
                lines_destroyed+=1
            else:
                stk.append(line)
        j=BOARD_HEIGHT-1
        while len(stk)>0:
            self.color[j] = stk.pop()
            j-=1
        self.score+=lines_destroyed
                
            



class Block:

    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],  
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]


    def __init__(self, x, y, board):
        self.x = x
        self.y = y
        self.rot = 0
        self.board = board
        #self.typ = random.randint(0,len(self.figures)-1)
        self.typ = 3
        self.col = random.randint(1,len(colors)-1)

    def intersects(self):
        for p in self.image():
            x = self.x + p % 4
            y = self.y + p // 4
            if y<0 or y>=BOARD_HEIGHT or x<0 or x>=BOARD_WIDTH or self.board.color[y][x]>0:
                return True
        return False

    def image(self):
        return self.figures[self.typ][self.rot]

    def rotate(self):
        old_rot=self.rot
        self.rot = (self.rot+1)%(len(self.figures[self.typ]))
        if self.intersects():
            self.rot=old_rot

    def move_right(self):
        self.x+=1
        if self.intersects():
            self.x-=1
 
    def move_left(self):
        self.x-=1
        if self.intersects():
            self.x+=1

    def move_down(self):
        self.y+=1
        if self.intersects():
            self.y-=1
            self.board.freeze()




        
        