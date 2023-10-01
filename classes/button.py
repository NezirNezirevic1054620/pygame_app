class Button:
    def __init__(self, image, x_position, y_position):
        self.image = image
        self.x_position = x_position
        self.y_position = y_position

    def draw(self, canvas):
        canvas.blit(self.image)
