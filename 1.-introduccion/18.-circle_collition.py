import sys
import math
import pygame

pygame.init()

width = 600
height = 600

surface = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('Colisión')

#RGB
white = (255, 255, 255)
red = (134, 45, 83)
green = (52, 157, 89)
blue = (59,87,181)
black = (0, 0, 0)

image1 = pygame.image.load('images/medium_circle.png')
rect1 = image1.get_rect()
rect1.center = (width // 2, height // 2)

surface2 = pygame.Surface( (rect1.width, rect1.height), pygame.SRCALPHA )
surface2.fill( (0, 0, 0, 50) )
rect2 = surface2.get_rect()
rect2.center = rect1.center

image2 = pygame.image.load('images/medium_circle.png')
rect3 = image2.get_rect()

font = pygame.font.Font('freesansbold.ttf', 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)

    rect3.center = pygame.mouse.get_pos()

    surface.blit(image1, rect1)
    surface.blit(surface2, rect2)
    surface.blit(image2, rect3)

    message = ''

    #dist = raiz cuadrada de = x * x + y * y
    #x = x1 - x2
    #y = y1 - y2
    dist = math.hypot(rect1.x - rect3.x, rect1.y - rect3.y)

    pygame.draw.line(surface, black, rect1.center, rect3.center, 2)
    message = 'La distancia es {} pixeles'.format( str(int(dist)) )

    if dist < (64 + 64):
        message = 'Existe una colisión'

    text = font.render(message, True, blue)
    rect4 = text.get_rect()
    rect4.midtop = (width // 2, 50)

    surface.blit(text, rect4)

    pygame.display.update()
