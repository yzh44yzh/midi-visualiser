import pygame
import midi_reader
import visualiser

FPS = 110
WIDTH = 1500
HEIGHT = 1000
WHITE_COLOR = (255, 255, 255)

pygame.init()
pygame.display.set_caption('MIDI Visualiser')

clock = pygame.time.Clock()
surface = pygame.display.set_mode((WIDTH, HEIGHT))

mfp = midi_reader.MidiFileParser('../midi/cold_forest_2_voice_1.mid', 110.5)
  
vis = visualiser.Visualiser(surface)
# vis.init_random_circles(7)
vis.add_events(mfp.get_events())

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
