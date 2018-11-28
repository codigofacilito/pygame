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

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                message = 'Izquierda'

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                message = 'Derecha'

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                message = 'Abajo'

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                message = 'Arriba'

            print(message)

        if event.type == pygame.KEYUP:
            #print('Tecla liberada!')
            pass

    surface.fill(white)
    pygame.display.update()
