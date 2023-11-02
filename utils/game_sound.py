import pygame
from pygame import mixer

pygame.mixer.init()


def background_music():
    background_sound_path = "sounds/bg_sound.mp3"
    mixer.music.load(background_sound_path)
    mixer.music.set_volume(0.2)
    mixer.music.play(-1)


def press_button_sound():
    press_button_sound_path = "sounds/press_sound.mp3"
    press_sound = pygame.mixer.Sound(press_button_sound_path)
    press_sound.play(0)


def game_over_sound():
    game_over_sound_path = "sounds/game_over_sound.mp3"
    mixer.music.load(game_over_sound_path)
    mixer.music.set_volume(0.2)
    mixer.music.play(0)


def collision_sound():
    collision_sound_path = "sounds/block_hit.mp3"
    collision_sound = pygame.mixer.Sound(collision_sound_path)
    mixer.music.set_volume(0.2)
    collision_sound.play(0)


def dead_sound():
    dead_sound_path = "sounds/space_shooter_dead.mp3"
    dead_sound = pygame.mixer.Sound(dead_sound_path)
    mixer.music.set_volume(0.2)
    dead_sound.play(0)


def win_sound():
    win_sound_path = "sounds/win_sound.mp3"
    mixer.music.load(win_sound_path)
    mixer.music.set_volume(0.2)
    mixer.music.play(0)
