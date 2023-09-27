import pygame
from pygame import mixer
from screens import main

pygame.init()
GAME_SPEED = 60
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
BACKGROUND_COLOR = (0, 0, 0)
pygame.display.set_caption("Fighter Jet-mania")
font = pygame.font.SysFont("arianblack", 45)

gameover_bg_img = pygame.image.load("images/gameover_bg.png")
gameover_fl_img = pygame.image.load("images/gameover_fl.png")

bg_music = "sounds/bg_sound.mp3"

clock = pygame.time.Clock()
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

text_color = (255, 255, 255)


# achtergrondmuziek functie
def background_music():
    pygame.mixer.init()
    mixer.music.load(bg_music)
    mixer.music.play(-1)


# Functie voor het game-over scherm
def game_over_screen():
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


# Functie om gebeurtenissen af te handelen
def handle_events():
    halting = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            halting = True
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                halting = True
                break
            if event.key == pygame.K_p:
                main.start_game_screen(canvas=canvas)
            if event.key == pygame.K_m:
                main.start_screen(canvas=canvas, font=font, text_color=text_color)
                pass
            if event.key == pygame.K_l:
                game_over_screen()

    return halting


background_music()
main.start_screen(canvas=canvas, font=font, text_color=text_color)
# Dit is de "game loop"
quit_program = False
while not quit_program:
    quit_program = handle_events()
    pygame.display.flip()
    clock.tick(GAME_SPEED)

pygame.quit()

print("Game over!")
