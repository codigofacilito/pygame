import sys
import pygame

pygame.init()

width = 600
height = 600

surface = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('Eventos del mouse')

#RGB
white = (255, 255, 255)
red = (134, 45, 83)

font = pygame.font.Font('freesansbold.ttf', 48)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pos_x, pos_y = pygame.mouse.get_pos() # Tupla (x, y)
    message = 'pos x : {} pos y : {}'.format(pos_x, pos_y)

    text = font.render(message, True, red)
    rect = text.get_rect()
    rect.center = (width // 2, height // 2)

    surface.fill(white)
    surface.blit(text, rect)
    pygame.display.update()
