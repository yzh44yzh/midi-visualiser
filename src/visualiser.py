import pygame
import animations

class Visualiser:
    NUM_CIRCLES = 10

    def __init__(self, root_surface):
        self.root_surface = root_surface
        self.circles = []
        for i in range(self.NUM_CIRCLES):
            self.circles.append(animations.AnimCircle(
                root_surface.get_width(),
                root_surface.get_height()
            ))

    def update(self):
        for c in self.circles:
            c.update()
            self.root_surface.blit(c.surface, (0, 0))
