import pygame
import visualiser

FPS = 60
WIDTH = 1500
HEIGHT = 1000
WHITE_COLOR = (255, 255, 255)

pygame.init()
pygame.display.set_caption('MIDI Visualiser')

clock = pygame.time.Clock()
surface = pygame.display.set_mode((WIDTH, HEIGHT))
vis = visualiser.Visualiser(surface)

running = True
while(running):
    clock.tick(FPS)
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
            break

    surface.fill(WHITE_COLOR)
    vis.update()
    pygame.display.update()

pygame.quit()
