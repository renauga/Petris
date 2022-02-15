import random

colors = [(0,0,0), (255,0,0), (0,255,0), (0,0,255)]

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


    def image(self):
        return self.figures[self.typ][self.rot]

    def rotate(self):
        self.rot = (self.rot+1)%(len(self.figures[self.typ]))

    def move_right(self):
        self.x+=1
 
    def move_left(self):
        self.x-=1

    def move_down(self):
        self.y+=1




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
        
        