import pygame
from settings import display

player_width = 100
player_height = 100
playerImg = pygame.image.load('assets/spaceship.png')
playerImg = pygame.transform.scale(playerImg, (player_width, player_height))

def Player(player_x, player_y):
    display.blit(playerImg, (player_x, player_y))