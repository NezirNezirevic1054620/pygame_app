# import pygame
# import math
# from utils.game_sound import press_button_sound, game_over_sound
#
# pygame.init()
#
#
# def scrolling_background(
#         SCREEN_WIDTH,
#         SCREEN_HEIGHT,
#         GAME_SPEED,
#         canvas,
#         font,
#         text_color,
# ):
#     # module is geimpoorteerd binnen een functie en niet top level omdat er circular error
#     # plaatsvindt
#     from screens.screen import start_screen, game_over_screen
#
#     background = pygame.image.load("images/background.png").convert()
#     background_width = background.get_width()
#
#     # Define game variables
#     scroll = 0
#     screen_tiles = math.ceil(SCREEN_WIDTH / background_width) + 1
#     # Game loop
#     run = True
#     hours = 0
#     minutes = 0
#     seconds = 0
#     text = font.render(f"{hours}:{minutes}:{seconds}", True, (255, 255, 255), (0, 0, 0))
#     clock = pygame.time.Clock()
#
#     while run:
#         clock.tick(GAME_SPEED)
#
#         # Draw scrolling background
#         for i in range(0, screen_tiles):
#             canvas.blit(background, (i * background_width + scroll, 0))
#
#         # Scroll background
#         scroll -= 6
#
#         # Reset scroll
#         if abs(scroll) > background_width:
#             scroll = 0
#         seconds += 1
#         if seconds == 3600:
#             seconds = 0
#             minutes += 1
#         if minutes == 60:
#             minutes = 0
#             seconds = 0
#             hours += 1
#         canvas.blit(text, (470, 700))
#         text = font.render(
#             f"{hours}:{minutes}:{seconds // 60}", True, (255, 255, 255), (0, 0, 0)
#         )
#         pygame.display.flip()
#
#         # Event handler
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 break
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_m:
#                     run = False
#                     press_button_sound()
#                     start_screen(canvas=canvas, font=font, text_color=text_color)
#                     pygame.display.flip()
#                 if event.key == pygame.K_q:
#                     quit()
#                 if event.key == pygame.K_p:
#                     run = False
#                 if event.key == pygame.K_r:
#                     run = False
#                     press_button_sound()
#                     game_over_sound()
#                     game_over_screen(
#                         SCREEN_HEIGHT=SCREEN_HEIGHT,
#                         SCREEN_WIDTH=SCREEN_WIDTH,
#                         canvas=canvas,
#                         font=font,
#                         text_color=text_color
#                     )
