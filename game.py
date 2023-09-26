import pygame

pygame.init()
GAME_SPEED = 60
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
BACKGROUND_COLOR = (0, 0, 0)
pygame.display.set_caption("Fighter Jet-mania")
background_image = pygame.image.load("images/pygame_start_bg.png")
background_image2 = pygame.image.load("images/placeholder_img.png")
start_btn_img = pygame.image.load("images/start_btn.png")
exit_btn_img = pygame.image.load("images/exit_btn.png")
font = pygame.font.SysFont("arianblack", 45)
text_color = (255, 255, 255)

clock = pygame.time.Clock()
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Functie voor het game-over scherm
def game_over_screen():
    canvas.fill(BACKGROUND_COLOR)
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


# Functie om het startscherm te tonen
def start_screen():
    canvas.blit(background_image, (0, 0))
    play_text = "PRESS P TO PLAY"
    quit_text = "PRESS Q TO QUIT"
    start_btn = pygame.image.load("images/start_btn.png")
    exit_btn = pygame.image.load("images/exit_btn.png")
    play_game = font.render(play_text, True, text_color)
    quit_game = font.render(quit_text, True, text_color)
    canvas.blit(play_game, (365, 480))
    canvas.blit(quit_game, (370, 650))
    canvas.blit(start_btn, (360, 350))
    canvas.blit(exit_btn, (380, 520))


# Functie om het spel te starten
def start_game():
    canvas.blit(background_image2, (0, 0))
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
                start_game()
            if event.key == pygame.K_m:
                start_screen()
            if event.key == pygame.K_l:
                game_over_screen()

    return halting


start_screen()
# Dit is de "game loop"
quit_program = False
while not quit_program:
    quit_program = handle_events()
    pygame.display.flip()
    clock.tick(GAME_SPEED)

pygame.quit()

print("Game over!")
