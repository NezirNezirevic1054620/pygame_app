import pygame
import math
from view import screen

# from utils import timer

pygame.init()


def scrolling_background(
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    background_ingame,
    GAME_SPEED,
    canvas,
    font,
    text_color,
):
    background = pygame.image.load("images/background.png").convert()
    background_width = background.get_width()
    background_height = background.get_height()

    # Define game variables
    scroll = 0
    screen_tiles = math.ceil(SCREEN_WIDTH / background_width) + 1
    # Game loop
    run = True
    hours = 0
    mins = 0
    secs = 0
    text = font.render(f"{hours}:{mins}:{secs}", True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    clock = pygame.time.Clock()

    while run:
        clock.tick(1)

        # Draw scrolling background
        for i in range(0, screen_tiles):
            canvas.blit(background, (i * background_width + scroll, 0))

        # Scroll background
        scroll -= 6

        # Reset scroll
        if abs(scroll) > background_width:
            scroll = 0
        secs += 1
        canvas.blit(text, textRect)
        if secs == 60:
            secs = 0
            mins += 1
        if mins == 60:
            mins = 0
            secs = 0
            hours += 1
        text = font.render(f"{hours}:{mins}:{secs}", True, (255, 255, 255), (0, 0, 0))
        pygame.display.flip()

        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    run = False
                    screen.start_screen(canvas=canvas, font=font, text_color=text_color)
                    pygame.display.flip()
