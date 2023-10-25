import pygame
from classes.bullet import Bullet

pygame.init()


class Player(pygame.sprite.Sprite):
    HEIGHT = 768
    WIDTH = 1024

    bullet_image = pygame.image.load("images/rocket.png")

    def __init__(self, image, scale):
        super().__init__()
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale))
        )
        self.image.set_colorkey(None)
        self.rect = self.image.get_rect()
        self.rect.centerx = 150
        self.rect.bottom = Player.HEIGHT / 2
        self.plane_y_position = 0

    def update(self):
        self.plane_y_position = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.plane_y_position = -8
        if keystate[pygame.K_DOWN]:
            self.plane_y_position = +8
        self.rect.y += self.plane_y_position
        if self.rect.bottom > Player.HEIGHT:
            self.rect.bottom = Player.HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    def shoot(self, all_sprites, bullets):
        bullet = Bullet(self.rect.centerx, self.rect.top, self.bullet_image, 0.3)
        all_sprites.add(bullet)
        bullets.add(bullet)
