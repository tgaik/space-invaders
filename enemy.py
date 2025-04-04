import pygame
from settings import display

def enemyImg(resize):
    img = pygame.image.load('assets/enemy.png')
    return pygame.transform.scale(img, (resize, resize))

class Enemy:
    def __init__(self, x, y, d, speed):
        self.x = x
        self.y = y
        self.d = d
        self.x_dir = 1
        self.speed = speed

    def draw(self):
        display.blit(enemyImg(self.d), (self.x, self.y))

    def move(self):
        self.x += self.x_dir * self.speed

    def shift_down(self):
        self.y += self.d

    def update_speed(self, speed):
        self.speed = speed