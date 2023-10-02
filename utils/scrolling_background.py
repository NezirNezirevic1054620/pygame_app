import pygame
import math

pygame.init()

clock = pygame.time.Clock()


def scrolling_background(SCREEN_WIDTH, SCREEN_HEIGHT, background_ingame, GAME_SPEED, canvas):
    # Load image
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


        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    

pygame.quit()
