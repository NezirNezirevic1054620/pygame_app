import pygame

from utils import timer
from utils import scrolling_background

pygame.init()

background_image = pygame.image.load("images/pygame_start_bg.png")
background_ingame = pygame.image.load("images/background.png")
start_btn_img = pygame.image.load("images/start_btn.png")
exit_btn_img = pygame.image.load("images/exit_btn.png")
gameover_bg_img = pygame.image.load("images/gameover_bg.png")
gameover_fl_img = pygame.image.load("images/gameover_fl.png")
GAME_SPEED = 60


# Functie om het startscherm te tonen
def start_screen(canvas, font, text_color):
    canvas.blit(background_image, (0, 0))
    play_text = "PRESS P TO PLAY"
    quit_text = "PRESS Q TO QUIT"
    start_btn = pygame.image.load("images/start_btn.png")
    exit_btn = pygame.image.load("images/exit_btn.png")
    play_game = font.render(play_text, True, text_color)
    quit_game = font.render(quit_text, True, text_color)
    canvas.blit(play_game, (365, 480))
    canvas.blit(quit_game, (370, 650))
    canvas.blit(start_btn, (360, 350))
    canvas.blit(exit_btn, (380, 520))
    pygame.display.flip()


# functie om de game te starten
def start_game_screen(canvas, font, SCREEN_WIDTH, SCREEN_HEIGHT, text_color):
    canvas.blit(background_ingame, (0, 0))
    scrolling_background.scrolling_background(
        SCREEN_HEIGHT=SCREEN_HEIGHT,
        SCREEN_WIDTH=SCREEN_WIDTH,
        background_ingame=background_ingame,
        canvas=canvas,
        GAME_SPEED=GAME_SPEED,
        font=font,
        text_color=text_color,
    )
    pygame.display.flip()


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

    # initial positie van gameover_fl_img
    fl_x = 0
    fl_y = 0
    
    # snelheid
    fl_speed_x = 2
    fl_speed_y = 1


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    start_screen(canvas, font, text_color)
                    pygame.display.flip()

        canvas.blit(game_over_text, game_over_rect)
        canvas.blit(restart_text, restart_rect)
        pygame.display.flip()

        # beweeg gameover_fl_img
        fl_x += fl_speed_x
        fl_y += fl_speed_y

        # als gameover_fl_img buiten het scherm gaat, keert deze terug
        if fl_x >= SCREEN_WIDTH:
            fl_x = 0
        
        if fl_y >= SCREEN_HEIGHT:
            fl_y = 0

        canvas.blit(gameover_fl_img, (fl_x, fl_y))
        pygame.display.flip()