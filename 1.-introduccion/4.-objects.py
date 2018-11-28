import sys
import pygame

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode( (width, height) ) #surface
pygame.display.set_caption('Objetos')

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
    pygame.draw.rect(surface, red, (100, 100, 80, 40) )

    pygame.draw.circle(surface, green, (200, 300), 100 )

    pygame.draw.line(surface, blue, (100, 100), (200, 300), 2 )

    pygame.display.update()
