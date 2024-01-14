import pygame

import Patron


class Reketa:

    def __init__(self, x, y, w, h, speed, texture):
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.hit_box = self.texture.get_rect()
        self.hit_box.x = x
        self.hit_box.y = y
        self.patrons = []


    def render(self, window):
        window.blit(self.texture, (self.hit_box.x, self.hit_box.y))
        for patron in self.patrons:
            patron.render(window)





    def move(self):
        keys = pygame.key.get_pressed()
        for patron in self.patrons:
            patron.sped()

        if keys[pygame.K_d]:
            self.hit_box.x += self.speed



        if keys[pygame.K_a]:
            self.hit_box.x -= self.speed

        if keys[pygame.K_SPACE]:
            self.patrons.append(Patron.Patron(self.hit_box.x, self.hit_box.y, 50, 5, 3,"bullet.png" ))


