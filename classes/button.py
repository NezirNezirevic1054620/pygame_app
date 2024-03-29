import pygame


class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale))
        )
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, canvas):
        # draw button on screen
        draw_button = canvas.blit(self.image, (self.rect.x, self.rect.y))

        return draw_button
