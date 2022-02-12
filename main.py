import pygame
from pygame.locals import *
from world import *
from player import *

# Global Variables
screen_width = 1000
screen_height = 1000
clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Peace')


# world = World(world_data)
player = Player(100, screen_height - 130)

pygame.init()
run = True
while run:
    # sets the frame rate
    clock.tick(fps)

    # create image on the screen
    screen.blit(space_img, (0,0))

    # world.draw()
    player.update(screen_height, screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # update the display 
    pygame.display.update()

pygame.quit()