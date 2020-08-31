import random
import pygame
pygame.init()

screen_width = 500
screen_height = 500


class Paddle:
    
    def __init__(self):
        self.width = random.randint(120, 170)
        self.height = 15
        self.x = random.randint(0, screen_width - self.width)
        self.y = int(screen_height*.99)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Generates Random Color
        if self.color == (255, 255, 255):
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.dx = 12                                                                             # velocity in x direction

    def drawPaddle(self, display, x, y):
        pygame.draw.rect(display, self.color, (x, y, self.width, self.height))
        

    