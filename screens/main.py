import pygame

pygame.init()


background_image = pygame.image.load("images/pygame_start_bg.png")
background_image2 = pygame.image.load("images/placeholder_img.png")
start_btn_img = pygame.image.load("images/start_btn.png")
exit_btn_img = pygame.image.load("images/exit_btn.png")


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
def start_game_screen(canvas):
    canvas.blit(background_image2, (0, 0))
    pygame.display.flip()
