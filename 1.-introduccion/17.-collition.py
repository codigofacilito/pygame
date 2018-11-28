import sys
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

image1 = pygame.image.load('images/small_rectangle.png')
rect1 = image1.get_rect()
rect1.center = (width // 2, height // 2)

image2 = pygame.image.load('images/small_rectangle.png')
rect2 = image2.get_rect()

font = pygame.font.Font('freesansbold.ttf', 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)

    rect2.center = pygame.mouse.get_pos()

    surface.blit(image1, rect1)
    surface.blit(image2, rect2)

    message = ''

    if rect1.colliderect(rect2):
        sound = pygame.mixer.Sound('sounds/coin.wav')
        sound.play()

        message = 'Existe una colisión'

    text = font.render(message, True, blue)
    rect3 = text.get_rect()
    rect3.midtop = (width // 2, 50)

    surface.blit(text, rect3)

    pygame.display.update()
