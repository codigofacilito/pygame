import sys
import pygame

pygame.init()

width = 600
height = 600

surface = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('Eventos del teclado')

#RGB
white = (255, 255, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        print('Arriba')

    if pressed[pygame.K_a]:
        print('Izquierda')

    if pressed[pygame.K_s]:
        print('Abajo')

    if pressed[pygame.K_d]:
        print('Derecha')

    surface.fill(white)
    pygame.display.update()
