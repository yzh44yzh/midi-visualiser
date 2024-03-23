import pygame
import animations
import datetime

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
        self.events = events

    def create_circle(self, size, duration):
        return animations.AnimCircle(
            self.root_surface.get_width(),
            self.root_surface.get_height(),
            size,
            duration
        )

    def update(self):
        if self.events:
            now = datetime.datetime.now()
            next_event = self.events[0]
            process_next_event = False

            if self.last_event:
                diff = now - self.last_event.time
                diff = diff.seconds * 1_000_000 + diff.microseconds
                process_next_event = diff >= (self.last_event.duration * 1_000_000)
            else:
                process_next_event = True

            if process_next_event:
                self.last_event = next_event
                self.last_event.time = now
                # print(self.last_event)

                self.events = self.events[1:]
                circle = self.create_circle(self.last_event.velocity, 300) # self.last_event.duration * 150)
                self.circles.append(circle)

        drop = []
        for c in self.circles:
            if c.update():
                self.root_surface.blit(c.surface, (0, 0))
            else:
                drop.append(c)

        for d in drop:
            self.circles.remove(d)
