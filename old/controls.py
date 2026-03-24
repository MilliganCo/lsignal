import pygame
import time
from player import MODES, console_messages

# Переменные выделения мышью
selecting = False
selection_start = None
selection_rect = pygame.Rect(0, 0, 0, 0)
MAX_SELECTION_SIZE = 150

keys = {pygame.K_a: False, pygame.K_d: False}
start_time = {pygame.K_a: None, pygame.K_d: None}

def handle_input():
    global frequency, mode_index, selecting, selection_start
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                mode_index = max(0, mode_index - 1)
                console_messages.append(f"Mode changed to {MODES[mode_index]}")
            elif event.key == pygame.K_s:
                mode_index = min(2, mode_index + 1)
                console_messages.append(f"Mode changed to {MODES[mode_index]}")
            elif event.key in [pygame.K_a, pygame.K_d]:
                keys[event.key] = True
                start_time[event.key] = time.time()
        elif event.type == pygame.KEYUP:
            if event.key in keys:
                keys[event.key] = False
                start_time[event.key] = None
        elif event.type == pygame.MOUSEBUTTONDOWN:
            selecting = True
            selection_start = event.pos
            selection_rect.update(selection_start[0], selection_start[1], 0, 0)
        elif event.type == pygame.MOUSEBUTTONUP:
            selecting = False
            check_anomaly_selection()

    # Ускорение при удержании клавиш A/D
    for key in [pygame.K_a, pygame.K_d]:
        if keys[key]:
            elapsed_time = time.time() - start_time[key] if start_time[key] else 0
            speed_multiplier = 1 + min(int(elapsed_time // 2), 5)  # Каждые 2 секунды ускорение до x5
            frequency += (-1 if key == pygame.K_a else 1) * speed_multiplier
            frequency = max(500, min(1500, frequency))

def handle_mouse_selection(screen):
    global selecting, selection_start, selection_rect
    if selecting:
        selection_end = pygame.mouse.get_pos()
        if selection_end[1] > selection_start[1]:  # Только сверху-вниз
            selection_rect.update(
                selection_start[0], selection_start[1],
                min(abs(selection_end[0] - selection_start[0]), MAX_SELECTION_SIZE),
                min(abs(selection_end[1] - selection_start[1]), MAX_SELECTION_SIZE)
            )
            pygame.draw.rect(screen, (255, 255, 255), selection_rect, 2)

def check_anomaly_selection():
    """ Проверка попадания аномалии в выделенную область """
    global anomalies
    for anomaly in anomalies[:]:
        if selection_rect.collidepoint(anomaly["x"], anomaly["y"]):
            console_messages.append(f"Anomaly at {anomaly['freq']} Hz removed!")
            anomalies.remove(anomaly)
