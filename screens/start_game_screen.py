import pygame
import math
import random

from utils.game_sound import press_button_sound, game_over_sound
from screens.game_over_screen import game_over_screen
from screens.start_screen import start_screen
from classes.player import Player
from classes.json_controller import JsonController
from classes.timer import Timer

pygame.init()
gravity = 0.1
plane = pygame.image.load("images/vliegtuigje2.png")
enemy_image = pygame.transform.scale(
    pygame.image.load("images/vliegtuigje3.png"), (150, 80))
powerup = pygame.image.load("images/power-up-1000.png")
endgame = pygame.image.load("images/power-up-end.png")
ENEMY_WIDTH, ENEMY_HEIGHT = 150, 80
POWERUP_WIDHT, POWERUP_HEIGHT = 40, 40
ENDGAME_WIDHT, ENDGAME_HEIGHT = 40, 40
meteoriet = pygame.image.load('images/meteoriet.png')
score_json = "data/score.json"


# functie om random enemy positie te genereren
def generate_enemy_position(SCREEN_WIDTH, SCREEN_HEIGHT):
    enemy_x = SCREEN_WIDTH 
    enemy_y = random.randint(0, SCREEN_HEIGHT - ENEMY_HEIGHT)

    return enemy_x, enemy_y


def draw_obstacle(canvas, obstacle_x, obstacle_y):
    obstacle_rect = meteoriet.get_rect()
    canvas.blit(meteoriet, obstacle_x, obstacle_y)


# functie om enemy te drawen
def draw_enemy(canvas, enemy_x, enemy_y):
    canvas.blit(enemy_image, (enemy_x, enemy_y))


# power-up drawen
def draw_powerup(canvas, powerup_x, powerup_y):
    canvas.blit(powerup, (powerup_x, powerup_y))

# power up spawnen
def generate_powerup_position(SCREEN_WIDTH, SCREEN_HEIGHT):
    powerup_x = SCREEN_WIDTH -200
    powerup_y = random.randint(0, SCREEN_HEIGHT - POWERUP_HEIGHT)

    return powerup_x, powerup_y

#endgame drawen
def draw_endgame(canvas, endgame_x, endgame_y):
    canvas.blit(endgame, (endgame_x, endgame_y))

# end game spawnen
def generate_endgame_position(SCREEN_WIDHT, SCREEN_HEIGHT):
    endgame_x = SCREEN_WIDHT -100
    endgame_y = random.randint(0, SCREEN_HEIGHT - ENDGAME_HEIGHT)

    return endgame_x, endgame_y

# start game scherm
def start_game_screen(canvas, font, SCREEN_WIDTH, GAME_SPEED, SCREEN_HEIGHT, text_color):
    background = pygame.image.load("images/background.png").convert()
    background_width = background.get_width()

    # scrolling background variabelen
    scroll = 0
    screen_tiles = math.ceil(SCREEN_WIDTH / background_width) + 1

    # enemy variabelen
    enemies = []
    enemy_spawn_timer = 0

    powerups = []
    powerup_spawn_timer = 0

    gameender = []
    endgame_spawn_timer = 0

    # Game loop
    clock = pygame.time.Clock()
    score = 0
    score_counter = font.render(f'Score: {score}', True, (255, 255, 255))
    run = True
    all_sprites = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    player = Player(plane, 0.3)
    all_sprites.add(player)
    json = JsonController(score_json, "w")
    timer = Timer()

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

        canvas.blit(score_counter, (10, 10))
        timer.initialize(canvas=canvas, text_color=text_color, x=435, y=700, GAME_SPEED=GAME_SPEED)
        score += 100
        score_counter = font.render(
            f'Score: {score // 60}', True, (255, 255, 255))

        # Generate enemies en powerups and the final game ender

        powerup_spawn_timer += 1
        enemy_spawn_timer += 1
        endgame_spawn_timer += 1

        if enemy_spawn_timer >= 5 * GAME_SPEED:
            enemy_spawn_timer = 0
            enemy_x, enemy_y = generate_enemy_position(
                SCREEN_WIDTH, SCREEN_HEIGHT)
            enemies.append([enemy_x, enemy_y])


        updated_enemies = []
        updated_powerups = []
        updated_gameender = []

        if endgame_spawn_timer >= 10 * GAME_SPEED:
            endgame_spawn_timer = 0
            endgame_x, endgame_y = generate_endgame_position(SCREEN_WIDTH, SCREEN_HEIGHT)
            gameender.append([endgame_x, endgame_y])

        if powerup_spawn_timer >= 10 * GAME_SPEED:
            powerup_spawn_timer = 0
            powerup_x, powerup_y = generate_powerup_position(
                SCREEN_WIDTH, SCREEN_HEIGHT)
            powerups.append([powerup_x, powerup_y])

        for powerup_x, powerup_y in powerups:
            powerup_x -= 2 

            if powerup_x + POWERUP_WIDHT > 0:
                draw_powerup(canvas, powerup_x, powerup_y)
                updated_powerups.append([powerup_x, powerup_y])

        for endgame_x, endgame_y in gameender:
            endgame_x -= 4

            if endgame_x + ENDGAME_WIDHT > 0:
                draw_endgame(canvas, endgame_x, endgame_y)
                updated_gameender.append([endgame_x, endgame_y])

        for enemy_x, enemy_y in enemies:
            enemy_x -= 8  # beweegt naar links

            if enemy_x + ENEMY_WIDTH > 0:
                draw_enemy(canvas, enemy_x, enemy_y)
                updated_enemies.append([enemy_x, enemy_y])

            # Check for collision
            if player.rect.colliderect(pygame.Rect(enemy_x, enemy_y, ENEMY_WIDTH, ENEMY_HEIGHT)):
                # Handle collision
                json.write_data(score=score)
                run = False
                press_button_sound()
                game_over_sound()
                game_over_screen(
                    SCREEN_HEIGHT=SCREEN_HEIGHT,
                    SCREEN_WIDTH=SCREEN_WIDTH,
                    canvas=canvas,
                    font=font,
                    text_color=text_color
                )
                bullets.empty()
                enemies.clear()
                player.remove(all_sprites)
        enemies = updated_enemies
        powerups = updated_powerups
        gameender = updated_gameender

        for bullet in bullets:
            # Check for collision
            for enemy_x, enemy_y in enemies:
                if bullet.rect.colliderect(pygame.Rect(enemy_x, enemy_y, ENEMY_WIDTH, ENEMY_HEIGHT)):
                    # Handle collision
                    enemies.remove([enemy_x, enemy_y])
                    score += 100
                    score_counter = font.render(
                        f'Score: {score // 60}', True, (255, 255, 255))

        all_sprites.draw(canvas)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot(all_sprites=all_sprites, bullets=bullets)
                    all_sprites.update()
                if event.key == pygame.K_m:
                    run = False
                    press_button_sound()
                    start_screen(canvas=canvas)
                    pygame.display.flip()
                if event.key == pygame.K_q:
                    quit()
                if event.key == pygame.K_r:
                    run = False
                    press_button_sound()
                    game_over_sound()
                    game_over_screen(
                        SCREEN_HEIGHT=SCREEN_HEIGHT,
                        SCREEN_WIDTH=SCREEN_WIDTH,
                        canvas=canvas,
                        font=font,
                        text_color=text_color
                    )
        all_sprites.update()
