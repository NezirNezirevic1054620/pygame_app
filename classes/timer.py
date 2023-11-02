import pygame
from classes.text import Text

pygame.init()


class Timer:
    hours = 0
    minutes = 0
    seconds = 0

    def __init__(self):
        self.timer_text = f"Timer: {self.hours}:{self.minutes}:{self.seconds // 60}"

    # timer wordt geladen op het scherm
    def initialize(self, canvas, text_color, x, y, GAME_SPEED):
        clock = pygame.time.Clock()
        while True:
            clock.tick(GAME_SPEED)
            self.seconds += 1
            if self.seconds == 3600:
                self.seconds = 0
                self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.seconds = 0
                self.hours += 1
            text = Text(f"Timer: {self.hours}:{self.minutes}:{self.seconds // 60}", text_color, x, y)
            text.draw(canvas)
            break
