import pygame
import math
import random

from utils.game_sound import press_button_sound, game_over_sound, collision_sound, dead_sound, win_sound
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
meteorite_image = pygame.transform.scale(
    pygame.image.load("images/meteorite.png"), (100, 100))
METEORITE_WIDTH = meteorite_image.get_width()
METEORITE_HEIGHT = meteorite_image.get_height()
meteorite_rect = meteorite_image.get_rect()
powerup = pygame.image.load("images/power-up-1000.png")
ENEMY_WIDTH, ENEMY_HEIGHT = 150, 80
POWERUP_WIDHT, POWERUP_HEIGHT = 40, 40
ENDGAME_WIDHT, ENDGAME_HEIGHT = 40, 40
score_json = "data/score.json"
win_screen = pygame.image.load("images/you_win.png")


# health_bar = PlayerHealth(max_health=99, width=200, height=20, x=10, y=10)

def generate_meteorite_pos(SCREEN_WIDTH, SCREEN_HEIGHT):
    meteorite_x = SCREEN_WIDTH
    meteorite_y = random.randint(0, 600)

    return meteorite_x, meteorite_y


def draw_meteorite(canvas, meteorite_x, meteorite_y):
    canvas.blit(meteorite_image, (meteorite_x, meteorite_y))


# functie om random enemy positie te genereren
def generate_enemy_position(SCREEN_WIDTH, SCREEN_HEIGHT):
    enemy_x = SCREEN_WIDTH
    enemy_y = random.randint(0, SCREEN_HEIGHT - ENEMY_HEIGHT)

    return enemy_x, enemy_y


# functie om enemy te drawen
def draw_enemy(canvas, enemy_x, enemy_y):
    canvas.blit(enemy_image, (enemy_x, enemy_y))


# power-up drawen
def draw_powerup(canvas, powerup_x, powerup_y):
    canvas.blit(powerup, (powerup_x, powerup_y))


# power up spawnen
def generate_powerup_position(SCREEN_WIDTH, SCREEN_HEIGHT):
    powerup_x = SCREEN_WIDTH - 200
    powerup_y = random.randint(0, SCREEN_HEIGHT - POWERUP_HEIGHT)

    return powerup_x, powerup_y


# end game spawnen
def generate_endgame_position(SCREEN_WIDHT, SCREEN_HEIGHT):
    endgame_x = SCREEN_WIDHT - 100
    endgame_y = random.randint(0, SCREEN_HEIGHT - ENDGAME_HEIGHT)

    return endgame_x, endgame_y


# start game scherm
def start_game_screen(canvas, font, SCREEN_WIDTH, GAME_SPEED, SCREEN_HEIGHT, text_color):
    background = pygame.image.load("images/background.png").convert()
    background_width = background.get_width()

    # scrolling background variabelen
    scroll = 0
    screen_tiles = math.ceil(SCREEN_WIDTH / background_width) + 1

    # Meteorite variabelen
    meteorites = []
    meteorite_timer = 0

    # enemy variabelen
    enemies = []
    enemy_spawn_timer = 0

    # powerups variabelen
    powerups = []
    powerup_spawn_timer = 0

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
    json = JsonController(score_json, "r+")
    timer = Timer()

    collided_enemies = []
    collided_meteorites = []

    while run and player.health > 0:
        clock.tick(GAME_SPEED)

        for i in range(0, screen_tiles):
            canvas.blit(background, (i * background_width + scroll, 0))

        # Scroll background
        scroll -= 5

        # Reset scroll
        # abs functie verkrijgt absolute waarde van een nummer
        if abs(scroll) > background_width:
            scroll = 0

        canvas.blit(score_counter, (10, 10))
        timer.initialize(canvas=canvas, text_color=text_color,
                         x=435, y=700, GAME_SPEED=GAME_SPEED)
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

        # Generate powerups

        updated_enemies = []
        updated_powerups = []

        if powerup_spawn_timer >= 10 * GAME_SPEED:
            powerup_spawn_timer = 0
            powerup_x, powerup_y = generate_powerup_position(
                SCREEN_WIDTH, SCREEN_HEIGHT)
            powerups.append([powerup_x, powerup_y])

        for powerup_x, powerup_y in powerups[:]:
            powerup_x -= 2

            if powerup_x + POWERUP_WIDHT > 0:
                draw_powerup(canvas, powerup_x, powerup_y)
                updated_powerups.append([powerup_x, powerup_y])

        for enemy_x, enemy_y in enemies:
            enemy_x -= 8  # beweegt naar links

            if enemy_x + ENEMY_WIDTH > 0:
                draw_enemy(canvas, enemy_x, enemy_y)
                updated_enemies.append([enemy_x, enemy_y])

            # Check for collision
            if player.rect.colliderect(pygame.Rect(enemy_x, enemy_y, ENEMY_WIDTH, ENEMY_HEIGHT)):
                # Handle collision
                json.write_json(score=score)
                player.health -= 33  # Reduce health by 33%
                if player.health < 0:
                    player.health = 0  # Ensure health doesn't go below 0
                dead_sound()

                if player.health == 0:
                    game_over_sound()
                    bullets.empty()
                    enemies.clear()
                    player.remove(all_sprites)
                    game_over_screen(
                        SCREEN_HEIGHT=SCREEN_HEIGHT,
                        SCREEN_WIDTH=SCREEN_WIDTH,
                        canvas=canvas,
                        font=font,
                        text_color=text_color
                    )
                collided_enemies.append([enemy_x, enemy_y])
            else:
                pass

        enemies = updated_enemies
        enemies = [enemy for enemy in enemies if enemy not in collided_enemies]

        # Generate meteorites
        if meteorite_timer <= 0:
            meteorite_timer = random.randint(200, 400)
            meteorite_x, meteorite_y = generate_meteorite_pos(
                SCREEN_WIDTH, SCREEN_HEIGHT)
            meteorites.append([meteorite_x, meteorite_y])
        meteorite_timer -= 1

        updated_meteorites = []
        for meteorite_x, meteorite_y in meteorites:
            meteorite_x -= 6  # beweegt naar links

            if meteorite_x + METEORITE_WIDTH > 0:
                draw_meteorite(canvas, meteorite_x, meteorite_y)
                updated_meteorites.append([meteorite_x, meteorite_y])
            meteorites = updated_meteorites

            if player.rect.colliderect(pygame.Rect(meteorite_x, meteorite_y, METEORITE_WIDTH, METEORITE_HEIGHT)):
                # Handle collision
                json.write_json(score=score)
                player.health -= 33  # Reduce health by 33%
                if player.health < 0:
                    player.health = 0  # Ensure health doesn't go below 0
                dead_sound()

                if player.health == 0:
                    game_over_sound()
                    bullets.empty()
                    enemies.clear()
                    player.remove(all_sprites)
                    game_over_screen(
                        SCREEN_HEIGHT=SCREEN_HEIGHT,
                        SCREEN_WIDTH=SCREEN_WIDTH,
                        canvas=canvas,
                        font=font,
                        text_color=text_color
                    )
                collided_meteorites.append([meteorite_x, meteorite_y])
            else:
                pass

        meteorites = [
            meteorite for meteorite in meteorites if meteorite not in collided_meteorites]

        powerups = updated_powerups

        for bullet in bullets:
            # Check for collision
            for enemy_x, enemy_y in enemies:
                if bullet.rect.colliderect(pygame.Rect(enemy_x, enemy_y, ENEMY_WIDTH, ENEMY_HEIGHT)):
                    # Handle collision
                    enemies.remove([enemy_x, enemy_y])
                    score += 10000

                    score += 100
                    score_counter = font.render(
                        f'Score: {score // 60}', True, (255, 255, 255))

            for powerup_x, powerup_y in powerups:
                if bullet.rect.colliderect(pygame.Rect(powerup_x, powerup_y, POWERUP_WIDHT, POWERUP_WIDHT)):
                    powerups.remove([powerup_x, powerup_y])
                    score += 100000

        all_sprites.draw(canvas)

        # Draw the player's health bar
        if player.health > 0:
            player.draw_health_bar(canvas)

        pygame.display.flip()

        # als de score op 10,000 komt dan win je het spel
        if score >= 600000:
            run = False
            canvas.blit(win_screen, (0, 0))
            pygame.display.flip()
            win_sound()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    collision_sound()
                    player.shoot(all_sprites=all_sprites, bullets=bullets)
                    all_sprites.update()
                    score += 10000
                if event.key == pygame.K_m:
                    json.write_json(score=score)
                    run = False
                    press_button_sound()
                    start_screen(canvas=canvas)
                    pygame.display.flip()
                if event.key == pygame.K_q:
                    json.write_json(score=score)
                    quit()
                if event.key == pygame.K_r:
                    json.write_json(score=score)
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
