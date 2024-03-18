import pygame
import random

FPS = 60
WIDTH = 1500
HEIGHT = 1000
NUM_CIRCLES = 10
MIN_RADIUS = 50
MAX_RADIUS = 300
WHITE_COLOR = (255, 255, 255)

pygame.init()
pygame.display.set_caption('MIDI Visualiser')
clock = pygame.time.Clock()
surface = pygame.display.set_mode((WIDTH, HEIGHT))

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b, 128)

def random_point():
    x = random.randint(50, WIDTH - 50)
    y = random.randint(50, HEIGHT - 50)
    return (x, y)

def random_radius():
    return random.randint(MIN_RADIUS, MAX_RADIUS - 100)


class AnimCircle:
    def __init__(self):
        self.surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        # self.surface.set_alpha(128)
        self.color = random_color()
        self.point = random_point()
        self.radius = random_radius()

    def update(self):
        self.radius += 1
        if self.radius > MAX_RADIUS:
            self.color = random_color()
            self.radius = MIN_RADIUS
            self.point = random_point()

        self.surface.fill((255, 255, 255, 30))
        pygame.draw.circle(self.surface, self.color, self.point, self.radius)

circles = []
for i in range(NUM_CIRCLES):
    circles.append(AnimCircle())

running = True
while(running):
    clock.tick(FPS)
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
            break

    surface.fill(WHITE_COLOR)
    
    for c in circles:
        c.update()
        surface.blit(c.surface, (0, 0))
    
    pygame.display.update()

pygame.quit()
