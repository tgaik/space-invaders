import pygame

pygame.init()

width = 800
height = 600
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")

background = (0, 0, 0)
white = (255, 255, 255)
yellow = (241, 196, 15)
red = (255, 0, 0)