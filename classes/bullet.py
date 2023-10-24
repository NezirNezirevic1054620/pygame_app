import pygame

pygame.init()


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, image, scale):
        super().__init__()
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale))
        )
        self.image.set_colorkey(None)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.centery = y + 50
        self.speedy = +10

    def update(self):
        self.rect.x += self.speedy
        if self.rect.bottom < 0:
            self.kill()
