# import os
# import time
import pygame
import midi_reader
import visualiser

FPS = 110
WIDTH = 1280
HEIGHT = 720
WHITE_COLOR = (255, 255, 255)

# os.environ['SDL_VIDEO_WINDOW_POS'] = "20,50"
pygame.init()
pygame.display.set_caption('Cold Forest')

clock = pygame.time.Clock()
surface = pygame.display.set_mode((WIDTH, HEIGHT))
# surface.fill(WHITE_COLOR)
# pygame.display.update()

mfp = midi_reader.MidiFileParser('../midi/cold_forest_2_voice_1.mid', 110.5)
  
vis = visualiser.Visualiser(surface)
vis.add_events(mfp.get_events())

# need time to start screen capture
# time.sleep(10)

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
