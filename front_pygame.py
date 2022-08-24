from msilib.schema import Icon
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000, 500))
game_icon = pygame.image.load('assets\game_logo.png')
pygame.display.set_caption('Who are you?')
pygame.display.set_icon(game_icon)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()    
    