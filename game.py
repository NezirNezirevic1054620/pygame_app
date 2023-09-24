import pygame

pygame.init()
GAME_SPEED = 60
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
# Kleuren worden aangeven met een tuple van 3 getallen - rood, groen, blauw - tussen 0 en 255.
# 0, 0, 0 betekend geen kleurm, dus zwart.
BACKGROUND_COLOR = (0, 0, 0)
pygame.display.set_caption("Fighter Jet-mania")
background_image = pygame.image.load("images/pygame_start_bg.png")
background_image2 = pygame.image.load("images/placeholder_img.png")

font = pygame.font.SysFont("arianblack", 60)
text_color = (255, 255, 255)

clock = pygame.time.Clock()
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# startscherm van de game
def start_screen():
    canvas.blit(background_image, (0, 0))
    play_text = "PRESS P TO PLAY"
    quit_text = "PRESS Q TO QUIT"
    play_game = font.render(play_text, font, True, text_color)
    quit_game = font.render(quit_text, font, True, text_color)
    canvas.blit(play_game, (320, 350))
    canvas.blit(quit_game, (320, 450))


# als deze functie wordt opgeroept dan start de game
def start_game():
    canvas.blit(background_image2, (0, 0))
    pygame.display.flip()


def handle_events():
    halting = False
    # De lijst met "events" is een lijst met alle gebeurtenissen die
    # plaatsvonden sinds de vorige loop. Hier komen ook de toetsaanslagen
    # in te staan. Let op! De .get() methode haalt de lijst leeg.
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

    return halting


start_screen()

# Dit is de "game loop"
quit_program = False
while not quit_program:
    quit_program = handle_events()
    pygame.display.flip()
    clock.tick(GAME_SPEED)

print("Game over!")
