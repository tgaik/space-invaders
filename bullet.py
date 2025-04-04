import pygame
from settings import display, yellow

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.d = 10
        self.speed = -10

    def draw(self):
        pygame.draw.ellipse(display, yellow, (self.x, self.y, self.d, self.d))

    def move(self):
        self.y += self.speed

    def hit(self, x, y, d):
        return x < self.x < x + d and y + d > self.y > y