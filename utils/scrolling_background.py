import pygame
import math
from view import screen
from utils import timer

pygame.init()

clock = pygame.time.Clock()


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

    while run:
        clock.tick(GAME_SPEED)

        # Draw scrolling background
        for i in range(0, screen_tiles):
            canvas.blit(background, (i * background_width + scroll, 0))

        # Scroll background
        scroll -= 6

        # Reset scroll
        if abs(scroll) > background_width:
            scroll = 0
        timer.game_timer(
            canvas=canvas,
            font=font,
            SCREEN_WIDTH=SCREEN_WIDTH,
            SCREEN_HEIGHT=SCREEN_HEIGHT,
        )
        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    # screen.start_screen(canvas=canvas, font=font, text_color=text_color)
                    pass
                if event.type == pygame.K_q:
                    quit()
                    break
        pygame.display.flip()
