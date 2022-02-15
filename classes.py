import random

colors = [(0,0,0), (255,0,0), (0,255,0), (0,0,255)]


class Game:
    def __init__(self, height, width, side):
        self.height = height
        self.width = width
        self.side = side
        self.color = [[0]*self.width for i in range(self.height)]
        self.score = 0
        self.active_block = None

    def reset(self):
        print("BOARD RESET")
        self.__init__(20,15,40)

    def freeze(self):
        self.score+=1
        for p in self.active_block.image():
            x = self.active_block.x + p % 4
            y = self.active_block.y + p // 4
            self.color[y][x] = self.active_block.col
        self.active_block = None


class Block:

    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],  
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]


    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.rot = 0
        self.typ = random.randint(0,len(self.figures)-1)
        self.col = random.randint(1,len(colors)-1)

    def intersects(self, board:Game):
        for p in self.image():
            x = self.x + p % 4
            y = self.y + p // 4
            if y<0 or y>=board.height or x<0 or x>=board.width or board.color[y][x]>0:
                return True
        return False

    def image(self):
        return self.figures[self.typ][self.rot]

    def rotate(self,board):
        old_rot=self.rot
        self.rot = (self.rot+1)%(len(self.figures[self.typ]))
        if self.intersects(board):
            self.rot=old_rot

    def move_right(self,board):
        self.x+=1
        if self.intersects(board):
            self.x-=1
 
    def move_left(self,board):
        self.x-=1
        if self.intersects(board):
            self.x+=1

    def move_down(self,board):
        self.y+=1
        if self.intersects(board):
            self.y-=1
            board.freeze()




        
        