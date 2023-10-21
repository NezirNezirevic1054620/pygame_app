import pygame
from screens.start_screen import start_screen
from utils.game_sound import press_button_sound, background_music

gameover_bg_img = pygame.image.load("images/gameover_bg.png")
gameover_skullimage_img = pygame.image.load("images/gameover_skullimage.png")


# Functie voor het game-over scherm
def game_over_screen(canvas, font, text_color, SCREEN_WIDTH, SCREEN_HEIGHT):
    canvas.blit(gameover_bg_img, (0, 0))
    game_over_text = font.render("Game Over", True, text_color)
    game_over_rect = game_over_text.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    )

    restart_text = font.render("PRESS R TO RESTART", True, text_color)
    restart_rect = restart_text.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
    )

    # initial positie van gameover_skullimage_img
    skullimage_x = 0
    skullimage_y = 0

    # snelheid
    skullimage_speed_x = 3
    skullimage_speed_y = 2
    gameover = True

    while gameover:
        canvas.blit(gameover_bg_img, (0, 0))
        # beweeg gameover_skullimage_img
        skullimage_x += skullimage_speed_x
        skullimage_y += skullimage_speed_y
        # als gameover_skullimage_img buiten het scherm gaat, keert deze terug
        if skullimage_x >= SCREEN_WIDTH:
            skullimage_x = 0
        if skullimage_y >= SCREEN_HEIGHT:
            skullimage_y = 0

        canvas.blit(game_over_text, game_over_rect)
        canvas.blit(restart_text, restart_rect)
        canvas.blit(gameover_skullimage_img, (skullimage_x, skullimage_y))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    press_button_sound()
                    background_music()
                    start_screen(canvas=canvas)
                    pygame.display.flip()
                    gameover = False

        pygame.display.flip()
