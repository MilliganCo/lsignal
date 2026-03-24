import pygame
import time

keys = {pygame.K_a: False, pygame.K_d: False}
start_time = {pygame.K_a: None, pygame.K_d: None}


def handle_events(game_state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                game_state.change_mode("up")
            elif event.key == pygame.K_s:
                game_state.change_mode("down")
            elif event.key in [pygame.K_a, pygame.K_d]:
                keys[event.key] = True
                start_time[event.key] = time.time()

        elif event.type == pygame.KEYUP:
            if event.key in keys:
                keys[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            game_state.selecting = True
            game_state.selection_rect.x, game_state.selection_rect.y = event.pos
            game_state.selection_rect.width = game_state.selection_rect.height = 0

        elif event.type == pygame.MOUSEBUTTONUP:
            game_state.selecting = False
            check_anomaly_selection(game_state)

    for key in [pygame.K_a, pygame.K_d]:
        if keys[key]:
            elapsed_time = time.time() - start_time[key] if start_time[key] else 0
            speed = 1 + min(int(elapsed_time // 1.5), 10)  # Ускорение до x10
            if key == pygame.K_a:
                game_state.change_frequency("down", speed)
            elif key == pygame.K_d:
                game_state.change_frequency("up", speed)

    return True


def check_anomaly_selection(game_state):
    """ Удаление аномалий при выделении + прибавка характеристик """
    removed = []
    for anomaly in game_state.anomalies:
        if game_state.selection_rect.colliderect(
                pygame.Rect(anomaly.x, anomaly.y, anomaly.size * 5, anomaly.size * 5)):
            removed.append(anomaly)
            if anomaly.mode == "Light":
                game_state.player_stats["Интуиция"] += 5
            elif anomaly.mode == "Neutral":
                game_state.player_stats["Рассудок"] += 5
            elif anomaly.mode == "Dark":
                game_state.player_stats["Осознание"] += 5
            game_state.console_messages.append(f"Anomaly at {anomaly.freq} Hz removed!")

    for anomaly in removed:
        game_state.anomalies.remove(anomaly)
