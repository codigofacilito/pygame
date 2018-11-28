import os
import pygame

from .config import *

class Coin(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y, dir_images):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load( os.path.join(dir_images, 'coin.png') )

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

        self.vel_x = SPEED

    def update(self):
        self.rect.left -= self.vel_x

    def stop(self):
        self.vel_x = 0
