import pygame
import random

class AnimBase:

    PADDING = 150

    def __init__(self, width, height):
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        
    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b, 128)

    def random_point(self):
        x = random.randint(self.PADDING, self.surface.get_width() - self.PADDING)
        y = random.randint(self.PADDING, self.surface.get_height() - self.PADDING)
        return (x, y)


class AnimCircle(AnimBase):

    def __init__(self, width, height, size, duration):
        super().__init__(width, height)
        # self.surface.set_alpha(128)
        self.color = self.random_color()
        self.point = self.random_point()
        self.radius = size
        self.life = duration

    def update(self):
        self.radius += 1
        self.life -= 1

        self.surface.fill((255, 255, 255, 30))
        pygame.draw.circle(self.surface, self.color, self.point, self.radius)

        return self.life > 0
