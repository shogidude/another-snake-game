import pygame
from constants import GREEN, SNAKE_SIZE, BROWN, LIGHT_BROWN

class Snake:
    def __init__(self):
        self.positions = [(100, 100), (90, 100), (80, 100)]
        self.direction = pygame.K_RIGHT
        self.growing = False

    def head_position(self):
        return self.positions[0]

    def move(self):
        cur = self.head_position()
        x, y = cur
        if self.direction == pygame.K_UP:
            y -= SNAKE_SIZE
        elif self.direction == pygame.K_DOWN:
            y += SNAKE_SIZE
        elif self.direction == pygame.K_LEFT:
            x -= SNAKE_SIZE
        elif self.direction == pygame.K_RIGHT:
            x += SNAKE_SIZE
        new_head = (x, y)

        if self.growing:
            self.positions.insert(0, new_head)
            self.growing = False
        else:
            self.positions.insert(0, new_head)
            self.positions.pop()

    def change_direction(self, key):
        if key == pygame.K_UP and self.direction != pygame.K_DOWN:
            self.direction = key
        elif key == pygame.K_DOWN and self.direction != pygame.K_UP:
            self.direction = key
        elif key == pygame.K_LEFT and self.direction != pygame.K_RIGHT:
            self.direction = key
        elif key == pygame.K_RIGHT and self.direction != pygame.K_LEFT:
            self.direction = key

    def grow(self):
        self.growing = True

    def draw(self, surface):
        for index, position in enumerate(self.positions):
            color = GREEN
            if index == 0:
                color = BROWN  # Head color
            elif index == len(self.positions) - 1:
                color = LIGHT_BROWN  # Tail color
            rect = pygame.Rect((position[0], position[1]), (SNAKE_SIZE, SNAKE_SIZE))
            pygame.draw.rect(surface, color, rect)