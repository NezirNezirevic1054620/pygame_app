import pygame
from pygame import mixer
from view import screen

pygame.init()
GAME_SPEED = 60
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
BACKGROUND_COLOR = (0, 0, 0)
pygame.display.set_caption("Fighter Jet-mania")
font = pygame.font.SysFont("arianblack", 45)

bg_music = "sounds/bg_sound.mp3"

clock = pygame.time.Clock()
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

text_color = (255, 255, 255)


# achtergrondmuziek functie
def background_music():
    pygame.mixer.init()
    mixer.music.load(bg_music)
    mixer.music.play(-1)


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
                screen.start_game_screen(canvas=canvas)
            if event.key == pygame.K_m:
                screen.start_screen(canvas=canvas, font=font, text_color=text_color)
                pass
            if event.key == pygame.K_l:
                screen.game_over_screen(
                    canvas=canvas,
                    font=font,
                    text_color=text_color,
                    SCREEN_HEIGHT=SCREEN_HEIGHT,
                    SCREEN_WIDTH=SCREEN_WIDTH,
                )

    return halting


background_music()
screen.start_screen(canvas=canvas, font=font, text_color=text_color)
# Dit is de "game loop"
quit_program = False
while not quit_program:
    quit_program = handle_events()
    pygame.display.flip()
    clock.tick(GAME_SPEED)

pygame.quit()

print("Game over!")
