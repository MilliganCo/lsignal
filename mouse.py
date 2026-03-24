import pygame

def handle_mouse_events(game_state):
    """ Обрабатывает нажатия, движения и отпускание мыши """
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            game_state.selecting = True
            game_state.selection_start = event.pos
            game_state.selection_radius = 0  # Радиус круга

        elif event.type == pygame.MOUSEBUTTONUP:
            game_state.selecting = False
            check_anomaly_selection(game_state)

        elif event.type == pygame.MOUSEMOTION and game_state.selecting:
            mx, my = event.pos
            dx = mx - game_state.selection_start[0]
            dy = my - game_state.selection_start[1]
            game_state.selection_radius = min((dx ** 2 + dy ** 2) ** 0.5, 100)  # Ограничение радиуса 100 пикселей

def check_anomaly_selection(game_state):
    """ Удаляет аномалии при выделении + выделенные символы меняют цвет """
    removed = []
    for anomaly in game_state.anomalies:
        distance = ((anomaly.x - game_state.selection_start[0]) ** 2 +
                    (anomaly.y - game_state.selection_start[1]) ** 2) ** 0.5
        if distance <= game_state.selection_radius:
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

    # Теперь изменяем цвет символов в области выделения
    mode = game_state.modes[game_state.mode_index]
    highlight_color = (255, 255, 255) if mode == "Neutral" else (255, 255, 0)
    for y in range(0, 900, 20):
        for x in range(0, 1920, 10):
            if ((x - game_state.selection_start[0]) ** 2 + (y - game_state.selection_start[1]) ** 2) ** 0.5 <= game_state.selection_radius:
                game_state.eaten_positions.add((x, y))  # Меняем цвет символов
