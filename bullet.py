import pygame
from circleshape import CircleShape
from constants import BULLET_RADIUS, BULLET_SPEED


class Bullet(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, BULLET_RADIUS)
        self.velocity = pygame.Vector2(0, 0)
        self.speed = BULLET_SPEED

    def draw(self, screen):
        # Calculate the end position for the line
        direction = self.velocity.normalize() if self.velocity.length() != 0 else pygame.Vector2(1, 0)
        end_pos = self.position + direction * self.radius * 2  # Length of the line
        pygame.draw.line(screen, "red", self.position, end_pos, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
