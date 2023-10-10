import pygame

plane_x = 100
plane_y = 300
flying = False 
gravity = 0.1
friendly = pygame.transform.scale(pygame.image.load('vliegtuigje2.png'), (80, 60))
y_speed = 0

class Plane:
    
    def draw_plane():
        plane = pygame.draw.circle(screen, 'black',(plane_x, plane_y), 20)
        screen.blit(friendly, (plane_x - 40, plane_y - 30))
        return plane
    
    def move_plane(y_pos, speed, fly):
        if fly:
            speed += gravity
        else:
            speed -= gravity
        y_pos -= speed
        return y_pos, speed
    
