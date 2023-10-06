import pygame

pygame.init()


def game_timer(canvas, font, SCREEN_WIDTH, SCREEN_HEIGHT):
    done = False
    hours = 0
    minutes = 0
    seconds = 0
    text = font.render(f"{seconds}", True, (255, 255, 255), (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

    while not done:
        seconds += 1
        if seconds == 3600:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            seconds = 0
            hours += 1
        canvas.blit(text, text_rect)
        text = font.render(
            f"{hours}:{minutes}:{seconds // 60}", True, (255, 255, 255), (0, 0, 0)
        )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
