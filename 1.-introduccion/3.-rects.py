import sys
import pygame

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode( (width, height) ) #surface
pygame.display.set_caption('Rectangulos')

#RGB
white = (255, 255, 255)
red = (115, 38, 80)
green = (52, 157, 89)

rect = pygame.Rect(100, 150, 120, 60)
rect.center = ( width // 2, height // 2)

print(rect.x)
print(rect.y)

rect2 = (100, 100, 80, 40)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)

    pygame.draw.rect(surface, red, rect)
    pygame.draw.rect(surface, green, rect2)

    pygame.display.update()
