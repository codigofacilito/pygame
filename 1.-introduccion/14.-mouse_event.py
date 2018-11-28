import sys
import pygame

pygame.init()

width = 600
height = 600

surface = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('Eventos del mouse')

#RGB
white = (255, 255, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            print(event.pos)

            if event.button == 1:
                print('Clic Izquierda')

            if event.button == 2:
                print('Clic centro')

            if event.button == 3:
                print('Clic Derecha')

            if event.button == 4:
                print('Scroll hacia arriba')

            if event.button == 5:
                print('Scroll hacia abajo')

        if event.type == pygame.MOUSEBUTTONUP:
            #print('Botón liberado')
            pass


    surface.fill(white)
    pygame.display.update()
