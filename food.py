import pygame
import random
from constants import RED, SCREEN_SIZE, SNAKE_SIZE

class Food:
    def __init__(self):
        self.position = self.spawn()

    def spawn(self):
        x = random.randint(0, (SCREEN_SIZE[0] - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        y = random.randint(0, (SCREEN_SIZE[1] - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        return (x, y)

    def draw(self, surface):
        rect = pygame.Rect((self.position[0], self.position[1]), (SNAKE_SIZE, SNAKE_SIZE))
        pygame.draw.rect(surface, RED, rect)