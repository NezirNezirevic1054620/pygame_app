import pygame
import math
from view import screen

# from utils import timer

pygame.init()


def scrolling_background(
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    GAME_SPEED,
    canvas,
    font,
    text_color,
):
    background = pygame.image.load("images/background.png").convert()
    background_width = background.get_width()

    # Define game variables
    scroll = 0
    screen_tiles = math.ceil(SCREEN_WIDTH / background_width) + 1
    # Game loop
    run = True
    hours = 0
    mins = 0
    secs = 0
    text = font.render(f"{secs}", True, (255, 255, 255), (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    clock = pygame.time.Clock()

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
        secs += 1
        if secs == 3600:
            secs = 0
            mins += 1
        if mins == 60:
            mins = 0
            secs = 0
            hours += 1
        canvas.blit(text, text_rect)
        text = font.render(
            f"{hours}:{mins}:{secs // 60}", True, (255, 255, 255), (0, 0, 0)
        )
        pygame.display.flip()

        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    run = False
                    screen.start_screen(canvas=canvas, font=font, text_color=text_color)
                    pygame.display.flip()
                if event.key == pygame.K_q:
                    break
                if event.key == pygame.K_p:
                    run = False
                if event.key == pygame.K_o:
                    run = True
