import random

import pygame
class Astero:
    def __init__(self, x, y, w, h, speed, texture, ):
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.hit_box = self.texture.get_rect()
        self.hit_box.x = x
        self.hit_box.y = y



    def render(self, window):
        window.blit(self.texture, (self.hit_box.x, self.hit_box.y))



    def down(self, window):
        self.hit_box.y += self.speed






