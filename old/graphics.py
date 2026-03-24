import pygame
import random
from old.player import player_stats, knowledge, frequency, mode_index, MODES

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

COLORS = [WHITE, GREEN, RED, YELLOW, BLUE, PURPLE]
ANOMALY_COLORS = [CYAN, MAGENTA, RED]

# Шрифт ASCII
pygame.init()
pygame.font.init()
FONT = pygame.font.SysFont("Courier", 20)

# Отрисовка ASCII-шумов
def draw_ascii_noise(screen):
    screen.fill(BLACK)
    current_mode = MODES[mode_index]
    for y in range(0, 900, 20):
        for x in range(0, 1920, 10):
            char = random.choice(["#", ".", "*", " "])
            color = random.choice(
                COLORS if current_mode == "Neutral" else [WHITE, BLUE] if current_mode == "Light" else [RED, PURPLE]
            )
            text = FONT.render(char, True, color)
            screen.blit(text, (x, y))

# Отрисовка интерфейса
def draw_interface(screen):
    pygame.draw.rect(screen, BLACK, (0, 900, 1920, 180))
    info_text = FONT.render(
        f"Frequency: {frequency} Hz | Mode: {MODES[mode_index]} | Knowledge: {knowledge} | Stats: {player_stats}",
        True, WHITE
    )
    screen.blit(info_text, (20, 950))
