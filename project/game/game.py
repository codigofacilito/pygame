import os
import sys
import pygame
import random

from .config import *
from .platform import Platform
from .player import Player
from .wall import Wall
from .coin import Coin

class Game:
    def __init__(self):
        pygame.init()

        self.surface = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption(TITLE)

        self.running = True

        self.clock = pygame.time.Clock()

        self.font = pygame.font.match_font(FONT)

        self.dir = os.path.dirname(__file__)
        self.dir_sounds = os.path.join(self.dir, 'sources/sounds')
        self.dir_images = os.path.join(self.dir, 'sources/sprites')

    def start(self):
        self.menu()
        self.new()

    def new(self):
        self.score = 0
        self.level = 0
        self.playing = True
        self.background = pygame.image.load( os.path.join(self.dir_images, 'background.png') )

        self.generate_elements()
        self.run()

    def generate_elements(self):
        self.platform = Platform()
        self.player = Player(100, self.platform.rect.top - 200, self.dir_images)

        self.sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()

        self.sprites.add(self.platform)
        self.sprites.add(self.player)

        self.generate_walls()

    def generate_walls(self):

        last_position = WIDTH + 100

        if not len(self.walls) > 0:

            for w in range(0, MAX_WALLS):

                left = random.randrange(last_position + 200, last_position + 400)
                wall = Wall(left, self.platform.rect.top, self.dir_images)

                last_position = wall.rect.right

                self.sprites.add(wall)
                self.walls.add(wall)

            self.level += 1
            self.generate_coins()

    def generate_coins(self):
        last_position = WIDTH + 100

        for c in range(0, MAX_COINS):
            pos_x = random.randrange(last_position + 180, last_position + 300)

            coin = Coin(pos_x, 100, self.dir_images)

            last_position = coin.rect.right

            self.sprites.add(coin)
            self.coins.add(coin)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:
            self.player.jump()

        if key[pygame.K_r] and not self.playing:
            self.new()

    def draw(self):
        self.surface.blit(self.background, (0, 0))

        self.draw_text()

        self.sprites.draw(self.surface)

        pygame.display.flip()

    def update(self):
        if not self.playing:
            return

        wall = self.player.collide_with(self.walls)
        if wall:
            if self.player.collide_bottom(wall):
                self.player.skid(wall)
            else:
                self.stop()

        coin = self.player.collide_with(self.coins)
        if coin:
            self.score += 1
            coin.kill()

            sound = pygame.mixer.Sound(os.path.join(self.dir_sounds, 'coin.wav'))
            sound.play()

        self.sprites.update()

        self.player.validate_platform(self.platform)

        self.update_elements(self.walls)
        self.update_elements(self.coins)

        self.generate_walls()

    def update_elements(self, elements):
        for element in elements:
            if not element.rect.right > 0:
                element.kill()

    def stop(self):
        sound = pygame.mixer.Sound(os.path.join(self.dir_sounds, 'lose.wav'))
        sound.play()

        self.player.stop()
        self.stop_elements(self.walls)

        self.playing = False

    def stop_elements(self, elements):
        for element in elements:
            element.stop()

    def score_format(self):
        return 'Score : {}'.format(self.score)

    def level_format(self):
        return 'Level : {}'.format(self.level)

    def draw_text(self):
        self.display_text(self.score_format(), 36, BLACK, WIDTH // 2, TEXT_POSY)
        self.display_text(self.level_format(), 36, BLACK, 60, TEXT_POSY)

        if not self.playing:
            self.display_text('Perdiste', 60, BLACK, WIDTH // 2, HEIGHT // 2)
            self.display_text('Presiona r para comenzar de nuevo', 30, BLACK, WIDTH // 2, 50)

    def display_text(self, text, size, color, pos_x, pos_y):
        font = pygame.font.Font(self.font, size)

        text = font.render(text, True, color)
        rect = text.get_rect()
        rect.midtop = (pos_x, pos_y)

        self.surface.blit(text, rect)

    def menu(self):
        self.surface.fill(GREEN_LIGHT)
        self.display_text('Presiona una tecla para comenzar', 36, BLACK, WIDTH // 2, 10)

        pygame.display.flip()

        self.wait()

    def wait(self):
        wait = True

        while wait:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    wait = False
                    self.running = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYUP:
                    wait = False
