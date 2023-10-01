import pygame
from utils import timer

pygame.init()

background_image = pygame.image.load("images/pygame_start_bg.png")
background_image2 = pygame.image.load("images/placeholder_img.png")
start_btn_img = pygame.image.load("images/start_btn.png")
exit_btn_img = pygame.image.load("images/exit_btn.png")
gameover_bg_img = pygame.image.load("images/gameover_bg.png")
gameover_fl_img = pygame.image.load("images/gameover_fl.png")


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


# functie om de game te starten
def start_game_screen(canvas, font, SCREEN_WIDTH, SCREEN_HEIGHT):
    canvas.blit(background_image2, (0, 0))
    timer.game_timer(
        canvas=canvas, font=font, SCREEN_WIDTH=SCREEN_WIDTH, SCREEN_HEIGHT=SCREEN_HEIGHT
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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    start_screen()
                    pygame.display.flip()

        canvas.blit(game_over_text, game_over_rect)
        canvas.blit(restart_text, restart_rect)
        pygame.display.flip()
