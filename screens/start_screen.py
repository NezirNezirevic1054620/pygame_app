import pygame
from classes.button import Button
from classes.text import Text

pygame.init()

background_image = pygame.image.load("images/pygame_start_bg.png")
background_ingame = pygame.image.load("images/background.png")
start_btn_img = pygame.image.load("images/start_btn.png")
exit_btn_img = pygame.image.load("images/exit_btn.png")


def start_screen(canvas, font, text_color):
    canvas.blit(background_image, (0, 0))
    start_button = Button(360, 350, start_btn_img, 1)
    exit_button = Button(380, 520, exit_btn_img, 1)
    play_text = Text("PRESS P TO PLAY", (255, 255, 255), 365, 480)
    play_text.draw(canvas)
    quit_text = Text("PRESS Q TO QUIT", (255, 255, 255), 370, 650)
    quit_text.draw(canvas)
    start_button.draw(canvas)
    exit_button.draw(canvas)
