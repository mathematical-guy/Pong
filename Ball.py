import pygame
import random
pygame.init()

screen_width = 500
screen_height = 500


class Ball:
    def __init__(self):
        self.radius = random.randint(10, 20)                                                    # Random radius
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Generates Random Color
        if self.color == (255, 255, 255):
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.x = random.randint(self.radius, screen_width - self.radius)                                               # random intial x
        self.y = random.randint(self.radius, screen_height//3)                                           # random intial y
        self.dx = 10                                                                                      # velocity in x direction
        self.dy = 5    
                                                                                # velocity in y direction
    def drawBall(self, display, x, y):
        pygame.draw.circle(display, self.color, (x, y), self.radius)

    
    
    