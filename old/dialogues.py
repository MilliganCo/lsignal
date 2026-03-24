from player import frequency, mode_index, player_stats
from old.controls import console_messages

# Первый сценарный ход
def check_dialogue_trigger():
    if frequency == 872 and mode_index == 1:
        show_dialogue()

def show_dialogue():
    console_messages.append("[Радиоприемник]: Неизвестный голос шепчет: 'Ты слышишь меня?'")
    console_messages.append("1) 'Кто ты?' → (Осознание +10)")
    console_messages.append("2) 'Оставь меня в покое.' → (Рассудок +10)")
    console_messages.append("3) 'Я боюсь...' → (Интуиция +10, аномалия усиливается)")

    choice = input("Выберите вариант (1, 2, 3): ")
    if choice == "1":
        player_stats["Осознание"] += 10
        console_messages.append("Вы ощутили прилив ясности.")
    elif choice == "2":
        player_stats["Рассудок"] += 10
        console_messages.append("Вы отмахнулись от голоса.")
    elif choice == "3":
        player_stats["Интуиция"] += 10
        console_messages.append("Аномалия усилилась...")
