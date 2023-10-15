import pygame

pygame.init()


class Screen:
    def __init_(self, font, text_color, SCREEN_HEIGHT, SCREEN_WIDTH, canvas):
        self.font = font
        self.text_color = text_color
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.canvas = canvas
