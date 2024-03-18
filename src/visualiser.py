import pygame
import animations

class Visualiser:

    def __init__(self, root_surface):
        self.root_surface = root_surface
        self.events = []
        self.circles = []
        self.last_event = None

    def init_random_circles(self, num_circles = 5):
        for i in range(num_circles):
            self.circles.append(self.create_circle(True))

    def add_events(self, events):
        self.last_event = None
        self.events = events[0:5]
        self.events.reverse()

    def create_circle(self, endless):
        # TODO color and size according to Note Event
        return animations.AnimCircle(
            self.root_surface.get_width(),
            self.root_surface.get_height(),
            endless
        )

    def update(self):
        if self.last_event:
            # TODO check duration between events
            self.last_event = None
        elif self.events:
            # TODO keep current time
            self.last_event = self.events.pop()
            print(self.last_event)
            circle = self.create_circle(False)
            self.circles.append(circle)

        drop = []
        for c in self.circles:
            if c.update():
                self.root_surface.blit(c.surface, (0, 0))
            else:
                drop.append(c)

        for d in drop:
            self.circles.remove(d)
