import pygame
import random
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def break_up(self):
        if self.radius > 15:
            for _ in range(2):
                from asteroidfield import AsteroidField
                velocity = self.velocity.rotate(random.uniform(-30, 30)) * random.uniform(0.5, 1.5)
                AsteroidField.spawn(self, self.radius / 3, self.position, velocity)
        self.kill()
