import sys
import pygame

pygame.init()

width = 600
height = 600

surface = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('Mover imagen')

#RGB
white = (255, 255, 255)
red = (134, 45, 83)

image = pygame.image.load('images/medium_circle.png')
rect = image.get_rect()
rect.center = (width // 2, height // 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    rect.center = pygame.mouse.get_pos() #Tupla -> (x,y)

    surface.fill(white)
    surface.blit(image, rect)

    pygame.display.update()
