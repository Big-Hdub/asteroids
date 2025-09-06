import json
import os
import pygame

LEADERBOARD_FILE = "leaderboard.json"

def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    with open(LEADERBOARD_FILE, "r") as f:
        return json.load(f)

def save_score(name, score):
    leaderboard = load_leaderboard()
    leaderboard.append({"name": name, "score": score})
    leaderboard.sort(key=lambda x: x["score"], reverse=True)
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(leaderboard, f)

def display_leaderboard(screen, leaderboard):
    font = pygame.font.Font(None, 48)
    screen.fill((0, 0, 0))
    for i, entry in enumerate(leaderboard[:10]):
        text = font.render(f"{i+1}. {entry['name']} - {entry['score']}", True, (255, 255, 255))
        screen.blit(text, (100, 100 + i * 50))
    pygame.display.flip()
