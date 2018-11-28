import pygame

from .config import *

class Platform(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface( (WIDTH, 40) )
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = HEIGHT - 40
