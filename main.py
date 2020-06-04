import pygame
pygame.init()

win = pygame.display.set_mode((500, 300))
pygame.display.set_caption("First Game")

run = True

class Meep:
    def __init__(self, pos, size, vel):
        self.pos = pos
        self.size = size
        self.vel = vel

    def show(self):
        pygame.draw.rect(win, (255,0,0), shape)

    def moveLeft(self):
        self.pos[0] - vel

    def moveRight(self):
        self.pos[0] + vel

def playerCommands(keys):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel

## main method
while run:

    keys = pygame.key.get_pressed()

    playerCommands(keys)

    win.fill((0,0,0))
    shape = (x, y, width, height)
    pygame.display.update()

pygame.quit()

