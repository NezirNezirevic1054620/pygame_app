import pygame
import math
from utils.game_sound import press_button_sound, game_over_sound
from screens.game_over_screen import game_over_screen
from screens.start_screen import start_screen

pygame.init()
gravity = 0.1
plane = pygame.transform.scale(pygame.image.load('images/vliegtuigje2.png'), (150, 80))


# functie om vliegtuig te drawen
def draw_player(canvas, player_x, player_y):
    player = pygame.draw.circle(canvas, 'black', (player_x, player_y), 0)
    canvas.blit(plane, (player_x - 40, player_y - 30))
    return player


# functie om vliegtuig bewegend te krijgen
def move_player(y_pos, speed, fly):
    if fly:
        speed += gravity
    else:
        speed -= gravity
    y_pos -= speed
    return y_pos, speed


# start game scherm
def start_game_screen(canvas, font, SCREEN_WIDTH, GAME_SPEED, SCREEN_HEIGHT, text_color):
    background = pygame.image.load("images/background.png").convert()
    background_width = background.get_width()

    # vliegtuigplayer variabelen
    active = True
    player_x = 100
    player_y = 300
    flying = False
    y_speed = 0

    # scrolling background variabelen
    scroll = 0
    screen_tiles = math.ceil(SCREEN_WIDTH / background_width) + 1
    # Game loop
    hours = 0
    minutes = 0
    seconds = 0
    text = font.render(f"{hours}:{minutes}:{seconds}", True, (255, 255, 255), (0, 0, 0))
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(GAME_SPEED)

        for i in range(0, screen_tiles):
            canvas.blit(background, (i * background_width + scroll, 0))

        # Scroll background
        scroll -= 6

        # Reset scroll
        # abs functie verkrijgt absolute waarde van een nummer
        if abs(scroll) > background_width:
            scroll = 0

        seconds += 1
        # timer
        if seconds == 3600:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            seconds = 0
            hours += 1

        canvas.blit(text, (470, 700))

        text = font.render(
            f"{hours}:{minutes}:{seconds // 60}", True, (255, 255, 255), (0, 0, 0)
        )

        if active:
            draw_player(canvas=canvas, player_x=player_x, player_y=player_y)
            player_y, y_speed = move_player(player_y, y_speed, flying)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    flying = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    flying = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    run = False
                    active = False
                    press_button_sound()
                    start_screen(canvas=canvas)
                    pygame.display.flip()
                if event.key == pygame.K_q:
                    quit()
                if event.key == pygame.K_r:
                    run = False
                    active = False
                    press_button_sound()
                    game_over_sound()
                    game_over_screen(
                        SCREEN_HEIGHT=SCREEN_HEIGHT,
                        SCREEN_WIDTH=SCREEN_WIDTH,
                        canvas=canvas,
                        font=font,
                        text_color=text_color
                    )
