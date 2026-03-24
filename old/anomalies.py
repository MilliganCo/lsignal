import random
import pygame
from player import player_stats, console_messages

anomalies = []
anomaly_spawn_timer = 0

def update_anomalies():
    global anomaly_spawn_timer
    if anomaly_spawn_timer <= 0:
        new_anomaly = {
            "freq": random.randint(500, 1500),
            "mode": random.choice(["Light", "Neutral", "Dark"]),
            "x": random.randint(50, 1800),
            "y": random.randint(50, 850),
            "size": 1
        }
        anomalies.append(new_anomaly)
        console_messages.append(f"Anomaly detected at {new_anomaly['freq']} Hz in {new_anomaly['mode']} mode")
        anomaly_spawn_timer = random.randint(300, 700)
    else:
        anomaly_spawn_timer -= 1
