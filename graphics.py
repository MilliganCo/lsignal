import pygame
import random

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)

# Цвета для выделения в зависимости от режима
MODE_SELECTION_COLORS = {
    "Light": (0, 255, 255, 150),  # Сделали чуть ярче
    "Neutral": (255, 255, 255, 150),
    "Dark": (255, 0, 255, 150)
}

# Правильные палитры
MODE_COLORS = {
    "Light": [WHITE, BLUE],
    "Neutral": [(255, 255, 255), (0, 255, 0), (255, 255, 0)],
    "Dark": [RED, PURPLE]
}

pygame.init()
FONT = pygame.font.SysFont("Courier", 20)

def draw_game(screen, game_state):
    screen.fill(BLACK)

    mode = game_state.modes[game_state.mode_index]
    for y in range(0, 900, 20):
        for x in range(0, 1920, 10):
            if (x, y) in game_state.eaten_positions:
                continue
            char = random.choice(["#", ".", "*", " "])
            color = random.choice(MODE_COLORS[mode])
            text = FONT.render(char, True, color)
            screen.blit(text, (x, y))

    for anomaly in game_state.anomalies:
        if game_state.frequency == anomaly.freq and game_state.modes[game_state.mode_index] == anomaly.mode:
            color = (255, 0, 255)
            for i in range(anomaly.size):
                text = FONT.render("@", True, color)
                screen.blit(text, (anomaly.x + i * 5, anomaly.y))

    draw_interface(screen, game_state)
    draw_selection_overlay(screen, game_state)  # Выделение теперь сверху

def draw_interface(screen, game_state):
    pygame.draw.rect(screen, BLACK, (0, 900, 1920, 180))
    info_text = FONT.render(
        f"Freq: {game_state.frequency} Hz | Mode: {game_state.modes[game_state.mode_index]} | "
        f"Осознание: {game_state.player_stats['Осознание']} | "
        f"Рассудок: {game_state.player_stats['Рассудок']} | "
        f"Интуиция: {game_state.player_stats['Интуиция']}",
        True, WHITE
    )
    screen.blit(info_text, (20, 950))

def draw_selection_overlay(screen, game_state):
    """ Рисует круг поверх всех элементов """
    if game_state.selecting:
        selection_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)  # Отдельный слой
        selection_color = MODE_SELECTION_COLORS[game_state.modes[game_state.mode_index]]
        pygame.draw.circle(selection_surface, selection_color, game_state.selection_start, int(game_state.selection_radius))
        screen.blit(selection_surface, (0, 0))  # Теперь рисуется наверху
