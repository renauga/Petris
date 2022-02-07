import pygame, classes

pygame.init()

screen = pygame.display.set_mode((800,900))
WHITE = (255,255,255)
GRAY = (127,127,127)
BLACK = (0,0,0)
x0 = 100
y0 = 50



board = classes.Game(20,15,40)

def start():
    print("called")
    board.__init__(20,15,40)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start()
    for i in range(board.height):
        for j in range(board.width):
            pygame.draw.rect(screen,WHITE,[x0+board.side*j,y0+board.side*i,board.side, board.side],1)
            pygame.draw.rect(screen,board.color[i][j],[x0+board.side*j+1,y0+board.side*i+1,board.side-2, board.side-2])

    pygame.display.update()


pygame.quit()