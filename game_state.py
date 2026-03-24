import pygame

class GameState:
    def __init__(self):
        self.frequency = 1000
        self.mode_index = 1  # 0 - Light, 1 - Neutral, 2 - Dark
        self.modes = ["Light", "Neutral", "Dark"]
        self.console_messages = []
        self.anomalies = []
        self.selecting = False
        self.selection_rect = pygame.Rect(0, 0, 0, 0)
        self.selection_start = (0, 0)  # Сохранение координат начала выделения
        self.selection_radius = 0  # <-- Добавлен атрибут
        self.eaten_positions = set()  # Места, где символы были съедены аномалиями
        self.player_stats = {"Осознание": 100, "Рассудок": 100, "Интуиция": 100}

    def change_frequency(self, direction, speed=1):
        if direction == "up":
            self.frequency = min(1500, self.frequency + speed)
        elif direction == "down":
            self.frequency = max(500, self.frequency - speed)

    def change_mode(self, direction):
        if direction == "up":
            self.mode_index = max(0, self.mode_index - 1)
        elif direction == "down":
            self.mode_index = min(2, self.mode_index + 1)
