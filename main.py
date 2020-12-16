import pygame
import random

WIDTH = 
HEIGHT =
FPS = 


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()


running = True
while running:
    
    clock.tick(FPS)
   
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            running = False

   
    screen.fill(BLACK)
   
    pygame.display.flip()

pygame.quit()
