import random
import pygame

class Anomaly:
    MAX_SIZE = 10  # Максимальный размер аномалии

    def __init__(self, game_state):
        self.freq = random.randint(500, 1500)
        self.mode = random.choice(game_state.modes)
        self.x = random.randint(50, 1800)
        self.y = random.randint(50, 850)
        self.size = 1
        self.speed_x = random.choice([-3, 3])
        self.speed_y = random.choice([-3, 3])

        game_state.console_messages.append(
            f"Anomaly detected at {self.freq} Hz in {self.mode} mode"
        )

    def update(self, game_state):
        """ Движение, разрастание и исчезновение аномалии """
        if game_state.frequency != self.freq or game_state.modes[game_state.mode_index] != self.mode:
            return True  # Аномалия неактивна на другом уровне

        self.size += 1
        self.speed_x = max(1, self.speed_x - 0.1)
        self.speed_y = max(1, self.speed_y - 0.1)

        if self.size >= self.MAX_SIZE:
            game_state.console_messages.append(f"Anomaly at {self.freq} Hz vanished!")
            self.apply_damage(game_state)
            return False  # Удалить аномалию

        # Движение
        self.x += self.speed_x
        self.y += self.speed_y

        # Отскок от границ
        if self.x < 50 or self.x > 1800:
            self.speed_x *= -1
        if self.y < 50 or self.y > 850:
            self.speed_y *= -1

        return True  # Аномалия еще существует

    def apply_damage(self, game_state):
        """ Уменьшает характеристики игрока при исчезновении аномалии """
        if self.mode == "Light":
            game_state.player_stats["Осознание"] -= 5
        elif self.mode == "Neutral":
            game_state.player_stats["Рассудок"] -= 5
        elif self.mode == "Dark":
            game_state.player_stats["Интуиция"] -= 5

    def check_collision(self, rect):
        return rect.colliderect(pygame.Rect(self.x, self.y, self.size * 5, self.size * 5))
