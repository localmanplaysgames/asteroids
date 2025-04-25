import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        if self.radius == ASTEROID_MAX_RADIUS:
            colour = "red"
        elif self.radius == ASTEROID_MIN_RADIUS:
            colour = "yellow"
        else:
            colour = "orange"
        pygame.draw.circle(screen, colour, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        vel1 = self.velocity.rotate(angle * 1)
        vel2 = self.velocity.rotate(angle * -1)
        rad = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, rad)
        ast1.velocity = vel1 * 1.2
        ast2 = Asteroid(self.position.x, self.position.y, rad)
        ast2.velocity = vel2 * 1.2