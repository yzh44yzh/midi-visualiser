import pygame
import random

class AnimBase:

    def __init__(self, width, height):
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        
    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b, 128)

    def random_point(self):
        x = random.randint(50, self.surface.get_width() - 50)
        y = random.randint(50, self.surface.get_height() - 50)
        return (x, y)


class AnimCircle(AnimBase):

    MIN_RADIUS = 50
    MAX_RADIUS = 300

    def __init__(self, width, height):
        super().__init__(width, height)
        # self.surface.set_alpha(128)
        self.color = self.random_color()
        self.point = self.random_point()
        self.radius = self.random_radius()

    def random_radius(self):
        return random.randint(self.MIN_RADIUS, self.MAX_RADIUS - 100)

    def update(self):
        self.radius += 1
        if self.radius > self.MAX_RADIUS:
            self.color = self.random_color()
            self.radius = self.MIN_RADIUS
            self.point = self.random_point()

        self.surface.fill((255, 255, 255, 30))
        pygame.draw.circle(self.surface, self.color, self.point, self.radius)
