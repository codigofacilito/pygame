import sys
import pygame

pygame.init()

width = 600
height = 600

surface = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('Tiempo')

#RGB
white = (255, 255, 255)
red = (115, 38, 80)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    time = pygame.time.get_ticks() // 1000 #Milisegundos
    print(time)

    surface.fill(white)
    pygame.display.update()
