import pygame
import sys
from Naruto import Naruto

pygame.init()
clock = pygame.time.Clock()

screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Naruto")

naruto = pygame.sprite.GroupSingle()
naruto.add(Naruto())

# Ground
ground = pygame.Surface((1920, 200)).convert_alpha()
ground.fill("Brown")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('Grey')
    screen.blit(ground, (0, 900))
    naruto.draw(screen)
    naruto.update()

    pygame.display.flip()
    clock.tick(60)

