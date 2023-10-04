import pygame

pygame.init()


def game_timer(canvas, font, SCREEN_WIDTH, SCREEN_HEIGHT):
    done = False
    hours = 0
    mins = 0
    secs = 0
    text = font.render(f"{secs}", True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

    while not done:
        secs += 1
        if secs == 3600:
            secs = 0
            mins += 1
        if mins == 60:
            mins = 0
            secs = 0
            hours += 1
        canvas.blit(text, textRect)
        text = font.render(
            f"{hours}:{mins}:{secs // 60}", True, (255, 255, 255), (0, 0, 0)
        )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
