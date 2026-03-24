import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 1920, 1080
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Последний сигнал")

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
FONT = pygame.font.SysFont("Courier", 20)

# Частота сигнала
frequency = 1000
mode_index = 1  # 0 - Light, 1 - Neutral, 2 - Dark
MODES = ["Light", "Neutral", "Dark"]

# Характеристики игрока
player_stats = {"Light": 100, "Neutral": 100, "Dark": 100}

# Аномалии
anomalies = []
anomaly_spawn_timer = 0
knowledge = {"Light": 0, "Neutral": 0, "Dark": 0}
console_messages = []

# Мышь
selecting = False
selection_start = None
selection_rect = pygame.Rect(0, 0, 0, 0)
MAX_SELECTION_SIZE = 150

# Время удержания клавиш
key_hold_time = {pygame.K_a: 0, pygame.K_d: 0}
start_time = {pygame.K_a: None, pygame.K_d: None}


# Функция отрисовки ASCII-шумов
def draw_ascii_noise():
    SCREEN.fill(BLACK)
    current_mode = MODES[mode_index]
    for y in range(0, HEIGHT - 250, 20):
        for x in range(0, WIDTH, 10):
            char = random.choice(["#", ".", "*", " "])
            color = random.choice(
                COLORS if current_mode == "Neutral" else [WHITE, BLUE] if current_mode == "Light" else [RED, PURPLE])
            text = FONT.render(char, True, color)
            SCREEN.blit(text, (x, y))


# Функция отрисовки интерфейса
def draw_interface():
    pygame.draw.rect(SCREEN, BLACK, (0, HEIGHT - 150, WIDTH, 150))
    info_text = FONT.render(
        f"Frequency: {frequency} Hz | Mode: {MODES[mode_index]} | Knowledge - Light: {knowledge['Light']} Dark: {knowledge['Dark']} Neutral: {knowledge['Neutral']} | Stats - Light: {player_stats['Light']} Neutral: {player_stats['Neutral']} Dark: {player_stats['Dark']}",
        True, WHITE)
    SCREEN.blit(info_text, (20, HEIGHT - 30))
    for i, message in enumerate(console_messages[-5:]):
        console_text = FONT.render(message, True, WHITE)
        SCREEN.blit(console_text, (20, HEIGHT - 140 + i * 20))


# Функция обновления аномалий
def update_anomalies():
    global anomaly_spawn_timer
    if anomaly_spawn_timer <= 0:
        new_anomaly = {"freq": random.randint(500, 1500), "mode": random.choice(MODES),
                       "x": random.randint(50, WIDTH - 300), "y": random.randint(50, HEIGHT - 300),
                       "vx": random.choice([-15, 15]), "vy": random.choice([-15, 15]), "size": 1}
        anomalies.append(new_anomaly)
        console_messages.append(f"Anomaly detected at {new_anomaly['freq']} Hz in {new_anomaly['mode']} mode")
        anomaly_spawn_timer = random.randint(300, 700)
    else:
        anomaly_spawn_timer -= 1


# Функция обработки выделения мышью (только сверху-вниз)
def handle_mouse_selection():
    global selecting, selection_start
    if selecting:
        selection_end = pygame.mouse.get_pos()
        if selection_end[1] > selection_start[1]:  # Только сверху-вниз
            selection_rect.update(
                selection_start[0], selection_start[1],
                min(abs(selection_end[0] - selection_start[0]), MAX_SELECTION_SIZE),
                min(abs(selection_end[1] - selection_start[1]), MAX_SELECTION_SIZE)
            )
            pygame.draw.rect(SCREEN, WHITE, selection_rect, 2)


# Основной игровой цикл
running = True
keys = {pygame.K_a: False, pygame.K_d: False}
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                mode_index = max(0, mode_index - 1)
            elif event.key == pygame.K_s:
                mode_index = min(2, mode_index + 1)
            elif event.key == pygame.K_a:
                frequency = max(500, frequency - 1)  # Уменьшение частоты
            elif event.key == pygame.K_d:
                frequency = min(1500, frequency + 1)  # Увеличение частоты
        elif event.type == pygame.MOUSEBUTTONDOWN:
            selecting = True
            selection_start = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            selecting = False

    draw_ascii_noise()
    update_anomalies()
    handle_mouse_selection()
    draw_interface()
    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()
