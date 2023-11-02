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

        self.health = 99  # Initialize the player's health
        self.max_health = 99  # Define the maximum health
        self.health_bar_length = 99  # Define the length of the health bar

    # player positie wordt geupdated met keys
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

    # player shoot functie
    def shoot(self, all_sprites, bullets):
        bullet = Bullet(self.rect.centerx, self.rect.top,
                        self.bullet_image, 0.3)
        all_sprites.add(bullet)
        bullets.add(bullet)

    # health bar wordt aangemaakt
    def draw_health_bar(self, screen):
        bar_width = int((self.health / self.max_health)
                        * self.health_bar_length)
        bar_color = (0, 255, 0)  # Green when healthy

        # Draw the background of the health bar
        pygame.draw.rect(screen, (255, 0, 0), (self.rect.centerx -
                                               self.health_bar_length / 2, self.rect.top - 30, self.health_bar_length,
                                               20))

        # Draw the actual health bar
        pygame.draw.rect(screen, bar_color, (self.rect.centerx -
                                             self.health_bar_length / 2, self.rect.top - 30, bar_width, 20))

        font = pygame.font.Font(None, 36)
        text = font.render(f"Health: {self.health}", True, (255, 255, 255))
        screen.blit(text, (self.rect.centerx -
                           text.get_width() / 2, self.rect.top - 50))
