import pygame

from utils.scrolling_background import scrolling_background
from classes.button import Button
from utils.game_sound import press_button_sound, background_music

pygame.init()

background_image = pygame.image.load("images/pygame_start_bg.png")
background_ingame = pygame.image.load("images/background.png")
start_btn_img = pygame.image.load("images/start_btn.png")
exit_btn_img = pygame.image.load("images/exit_btn.png")
gameover_bg_img = pygame.image.load("images/gameover_bg.png")
gameover_skullimage_img = pygame.image.load("images/gameover_skullimage.png")
GAME_SPEED = 60


# Functie om het startscherm te tonen
def start_screen(canvas, font, text_color):
    canvas.blit(background_image, (0, 0))
    start_button = Button(360, 350, start_btn_img, 1)
    exit_button = Button(380, 520, exit_btn_img, 1)
    play_text = "PRESS P TO PLAY"
    quit_text = "PRESS Q TO QUIT"
    play_game = font.render(play_text, True, text_color)
    quit_game = font.render(quit_text, True, text_color)
    canvas.blit(play_game, (365, 480))
    canvas.blit(quit_game, (370, 650))
    start_button.draw(canvas)
    exit_button.draw(canvas)


# functie om de game te starten
def start_game_screen(canvas, font, SCREEN_WIDTH, SCREEN_HEIGHT, text_color):
    canvas.blit(background_ingame, (0, 0))
    scrolling_background(
        SCREEN_HEIGHT=SCREEN_HEIGHT,
        SCREEN_WIDTH=SCREEN_WIDTH,
        canvas=canvas,
        GAME_SPEED=GAME_SPEED,
        font=font,
        text_color=text_color,
    )


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
                    start_screen(canvas, font, text_color)
                    pygame.display.flip()
                    gameover = False

        pygame.display.flip()
