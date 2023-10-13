import pygame
from classes.button import Button

pygame.init()

background_image = pygame.image.load("images/pygame_start_bg.png")
background_ingame = pygame.image.load("images/background.png")
start_btn_img = pygame.image.load("images/start_btn.png")
exit_btn_img = pygame.image.load("images/exit_btn.png")


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
