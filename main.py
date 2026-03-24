import pygame
from game_state import GameState
from events import handle_events
from anomaly import Anomaly
from graphics import draw_game
from mouse import handle_mouse_events  # Новый модуль

# Инициализация Pygame
pygame.init()
WIDTH, HEIGHT = 1920, 1080
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Последний сигнал")

# Создание состояния игры
game_state = GameState()

running = True
while running:
    running = handle_events(game_state)  # Обрабатываем события клавиш
    handle_mouse_events(game_state)  # Обрабатываем события мыши

    if len(game_state.anomalies) < 5:  # Лимит аномалий
        game_state.anomalies.append(Anomaly(game_state))

    draw_game(SCREEN, game_state)  # Отрисовка игры
    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()
