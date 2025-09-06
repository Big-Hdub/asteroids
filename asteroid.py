import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def break_up(self):
        score = 10 * (ASTEROID_MAX_RADIUS / self.radius)
        if self.radius > 20:
            for i in range(2):
                from asteroidfield import AsteroidField
                velocity = self.velocity.rotate(-30) if i == 0 else self.velocity.rotate(30)
                velocity *= random.uniform(0.5, 1.5)
                AsteroidField.spawn(self, self.radius - ASTEROID_MIN_RADIUS, self.position, velocity)
        self.kill()
        return score
