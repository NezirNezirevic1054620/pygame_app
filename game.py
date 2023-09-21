import pygame

pygame.init()
GAME_SPEED = 60
LOGO_SPEED = 3
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
# Kleuren worden aangeven met een tuple van 3 getallen - rood, groen, blauw - tussen 0 en 255.
# 0, 0, 0 betekend geen kleurm, dus zwart.
BACKGROUND_COLOR = (0, 0, 0)
pygame.display.set_caption("Fighter Jet-mania")
background_image = pygame.image.load("images/pygame_start_bg.png")

font = pygame.font.SysFont("arialblack", 40)
text_color = (255, 255, 255)

clock = pygame.time.Clock()
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    canvas.blit(img, (x, y))


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
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                halting = True
                break

    return halting


# logo = pygame.image.load("images/ra_logo.png").convert_alpha()
# logo_rect = logo.get_rect()
# logo_speed = [LOGO_SPEED, LOGO_SPEED]

# Dit is de "game loop"
quit_program = False
while not quit_program:
    quit_program = handle_events()
    canvas.blit(background_image, (0, 0))
    draw_text("PRESS P TO PLAY", font, text_color, 312, 359)

    pygame.display.flip()
    clock.tick(GAME_SPEED)

print("Game over!")
