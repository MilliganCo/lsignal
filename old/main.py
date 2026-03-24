import pygame
from graphics import draw_ascii_noise, draw_interface
from old.anomalies import update_anomalies
from old.controls import handle_input, handle_mouse_selection
from old.dialogues import check_dialogue_trigger

# Инициализация Pygame
pygame.init()
WIDTH, HEIGHT = 1920, 1080
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Последний сигнал")

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    handle_input()
    update_anomalies()
    check_dialogue_trigger()

    draw_ascii_noise(SCREEN)
    handle_mouse_selection(SCREEN)
    draw_interface(SCREEN)

    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()
