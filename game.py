import pygame
from utils.game_sound import background_music, press_button_sound, game_over_sound
from screens.start_game_screen import start_game_screen
from screens.game_over_screen import game_over_screen
from screens.start_screen import start_screen

pygame.init()
GAME_SPEED = 60
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
BACKGROUND_COLOR = (0, 0, 0)
pygame.display.set_caption("Fighter Jet-mania")
font = pygame.font.SysFont("arianblack", 45)

clock = pygame.time.Clock()
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

text_color = (255, 255, 255)


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
                press_button_sound()
                start_game_screen(
                    canvas=canvas,
                    font=font,
                    SCREEN_WIDTH=SCREEN_WIDTH,
                    GAME_SPEED=GAME_SPEED,
                    SCREEN_HEIGHT=SCREEN_HEIGHT,
                    text_color=text_color
                )
                pygame.display.flip()
            if event.key == pygame.K_m:
                press_button_sound()
                start_screen(
                    canvas=canvas,
                    font=font,
                    text_color=text_color,
                )
                pygame.display.flip()
            if event.key == pygame.K_r:
                press_button_sound()
                game_over_sound()
                game_over_screen(
                    canvas=canvas,
                    font=font,
                    text_color=text_color,
                    SCREEN_HEIGHT=SCREEN_HEIGHT,
                    SCREEN_WIDTH=SCREEN_WIDTH,
                )

    return halting


background_music()
start_screen(canvas=canvas, font=font, text_color=text_color)
# Dit is de "game loop"
quit_program = False
while not quit_program:
    quit_program = handle_events()
    pygame.display.flip()
    clock.tick(GAME_SPEED)

pygame.quit()

print("Game over!")
