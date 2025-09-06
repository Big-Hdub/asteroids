import pygame

def show_menu(screen):
    font = pygame.font.Font(None, 74)
    options = ["Start Game", "Leaderboard", "Difficulty", "Quit"]
    selected = 0
    running = True

    while running:
        screen.fill((0, 0, 0))
        for i, option in enumerate(options):
            color = (255, 255, 0) if i == selected else (255, 255, 255)
            text = font.render(option, True, color)
            screen.blit(text, (100, 100 + i * 100))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    return options[selected]

# Usage in your main loop:
# choice = show_menu(screen)
# if choice == "Start Game":
#     # start the game
