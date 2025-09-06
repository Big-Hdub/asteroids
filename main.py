import dis
import pygame
import time
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet
from score import draw_score

# Usage in your main loop:
# choice = show_menu(screen)
# if choice == "Start Game":
#     # start the game
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    game_state = "MENU"

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable, bullets)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Bullet.containers = (updatable, drawable, bullets)

    dt = 0

    while game_state != "QUIT":
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        if game_state == "GAME OVER":
            font = pygame.font.Font(None, 74)
            screen.fill((0, 0, 0))
            color = (255, 50, 100)
            text = font.render("GAME OVER!! Try again if you dare.", True, color)
            screen.blit(text, (200, 300))
            pygame.display.flip()
            time.sleep(3)
            game_state = "MENU"
            continue

        elif game_state == "MENU":
            from menu import show_menu
            choice = show_menu(screen)
            if choice == "Start Game":
                game_state = "PLAYING"
            elif choice == "Leaderboard":
                from leaderboard import load_leaderboard, display_leaderboard
                leaderboard = load_leaderboard()
                display_leaderboard(screen, leaderboard)
                time.sleep(3)
            elif choice == "Difficulty":
                pass  # Implement difficulty settings
            elif choice == "Quit":
                game_state = "QUIT"
            continue
        elif game_state == "PLAYING":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_state = "QUIT"

            updatable.update(dt)

            for asteroid in asteroids:
                if asteroid.is_colliding(player):
                    game_state = "GAME OVER"
                    for obj in drawable:
                        obj.kill()
                    break
            for bullet in bullets:
                for asteroid in asteroids:
                    if bullet.is_colliding(asteroid):
                        player.score += asteroid.break_up()
                        bullet.kill()
                        break

            screen.fill("black")

            for obj in drawable:
                obj.draw(screen)
            draw_score(screen, player.score)

        pygame.display.flip()



if __name__ == "__main__":
    main()
