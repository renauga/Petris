import random
colors = [(255,0,0), (0,255,0), (0,0,255)]


class Game:
    def __init__(self, height, width, side):
        self.height = height
        self.width = width
        self.side = side
        self.color = []
        self.score = 0
        self.active_block = None
        for i in range(self.height):
            self.color.append([])
            for j in range(self.width):
                self.color[i].append(colors[random.randint(0,len(colors)-1)])
        
        