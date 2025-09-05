import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    dt = 0
    player = Player(screen.get_width() // 2, screen.get_height() // 2)
    updatable = pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)
    player.containers = updatable, drawable

    # Main game loop
    running = True
    while running:
        dt = clock.tick(60) / 1000  # Limit to 60 FPS and get delta time
        screen.fill((0, 0, 0))  # Clear screen with black
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)
        pygame.display.flip()  # Update the full display Surface to the screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == "__main__":
    main()
