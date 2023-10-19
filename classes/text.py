import pygame

pygame.init()


class Text:
    font = pygame.font.SysFont("arianblack", 45)

    def __init__(self, text, text_color, x, y):
        self.text = text
        self.text_color = text_color
        self.x = x
        self.y = y

    def draw(self, canvas):
        text = self.font.render(self.text, True, self.text_color)
        action = canvas.blit(text, (self.x, self.y))

        return action
