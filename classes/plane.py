import pygame



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
    
