import sys
import pygame

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode( (width, height) ) #surface
pygame.display.set_caption('Poligonos')

#RGB
white = (255, 255, 255)
red = (115, 38, 80)
green = (52, 157, 89)
blue = (59,87,181)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)

    #draw
    #1.- Donde se pintará la figura
    #2.- De qué color será la figura

    #Triangulo
    pygame.draw.polygon(surface, green,
                ( (0, 400), (100, 300), (200, 400) ))

    #Pentagono
    pygame.draw.polygon(surface, red, (
        (146, 0),
        (291, 106),
        (236, 277),
        (56, 277),
        (0, 106)
    ))

    pygame.display.update()
