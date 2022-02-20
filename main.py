import pygame as pg
from pygame.locals import *
from world import *
from player import *
from button import *

# Global Variables
screen_width = 1000
screen_height = 1000
clock = pygame.time.Clock()
fps = 60
main_menu = True 

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Get Bob Home')

#load images
sun_img = pygame.image.load('img/background/sun.png')
bg_img = pygame.image.load('img/background/sky.png')
# start_img = pg.transform.scale(pygame.image.load('img/buttons/start.png'), (200,100))
# exit_img = pg.transform.scale(pygame.image.load('img/buttons/quit.png'), (200,100))
start_img = pygame.image.load('img/buttons/start_btn.png')
exit_img = pygame.image.load('img/buttons/exit_btn.png')
space_img = pygame.image.load('img/background/space.png')
menu_img = pygame.image.load('img/background/m.png')


#Level1
world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1], 
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1], 
[1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1], 
[1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


player = Player(100, screen_height - 130)
world = World(world_data)
pygame.init()

# Create Buttons
start_button = Button(screen_width // 2 - 350, screen_height // 2, start_img)
exit_button = Button(screen_width // 2 + 150, screen_height // 2, exit_img)

# Texts
font = pygame.font.Font('Fontrust.otf', 125)
font1 = pygame.font.Font('Fontrust.otf', 30)
title = font.render('Get Bob Home', True, (0,0,0))
credit = font1.render('made by TaeGyun Lim', True, (0,0,0))

run = True
while run:
    # sets the frame rate
    clock.tick(fps)

    
    # create image on the screen
    screen.blit(bg_img, (0, 0))
    screen.blit(sun_img, (100, 100))

    if main_menu == True:
        screen.blit(title, (250,125))
        screen.blit(credit, (400,900))
        if exit_button.draw(screen):
            run = False
        if start_button.draw(screen):
            main_menu = False
    else:

        world.draw(screen)
        player.update(screen_height, screen, world)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # update the display 
    pygame.display.update()

pygame.quit()