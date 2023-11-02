class PlayerHealth:

    def __init__(self, max_health, width, height, x, y):
        self.max_health = max_health
        self.current_health = max_health
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.health_color = (0, 255, 0)
        self.health_background_color = (255, 0, 0)

    def decrease_health(self, amount):
        self.current_health -= amount
        if self.current_health < 0:
            self.current_health = 0

    def increase_health(self, amount):
        self.current_health += amount
        if self.current_health > self.max_health:
            self.current_health = self.max_health
