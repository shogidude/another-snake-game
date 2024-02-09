import pygame
from snake import Snake
from food import Food
from constants import SCREEN_SIZE, BLACK

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = 0  # Initialize score
        self.font = pygame.font.SysFont(None, 35)  # Initialize font
        self.game_over = False  # Initialize game over flag
        self.paused = False  # Initialize paused flag

    def check_game_over(self):
        if (self.snake.head_position()[0] < 0 or self.snake.head_position()[0] >= SCREEN_SIZE[0] or
            self.snake.head_position()[1] < 0 or self.snake.head_position()[1] >= SCREEN_SIZE[1] or
            self.snake.head_position() in self.snake.positions[1:]):
            self.game_over = True

    def flash_screen(self):
        inverted_color = (255 - BLACK[0], 255 - BLACK[1], 255 - BLACK[2])
        self.screen.fill(inverted_color)
        pygame.display.flip()
        pygame.time.wait(500)

    def display_game_over(self):
        self.screen.fill(BLACK)
        game_over_font = pygame.font.SysFont(None, 90)
        game_over_text = game_over_font.render('GAME OVER', True, (255, 255, 255))
        text_rect = game_over_text.get_rect(center=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2))
        self.screen.blit(game_over_text, text_rect)
        pygame.display.flip()

    def reset_game(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_over = False

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if self.game_over and event.key == pygame.K_SPACE:
                        self.reset_game()
                    elif not self.game_over:
                        if event.key == pygame.K_SPACE:
                            self.paused = not self.paused
                        elif not self.paused:
                            self.snake.change_direction(event.key)

            if not self.game_over and not self.paused:
                self.snake.move()
                self.check_game_over()
            elif self.paused:
                pause_font = pygame.font.SysFont(None, 90)
                pause_text = pause_font.render('PAUSED', True, (255, 255, 255))
                text_rect = pause_text.get_rect(center=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2))
                self.screen.blit(pause_text, text_rect)
                pygame.display.flip()

            if not self.paused:
                if self.game_over:
                    self.flash_screen()
                    self.display_game_over()
                else:
                    if self.snake.head_position() == self.food.position:
                        self.snake.grow()
                        self.food.position = self.food.spawn()
                        self.score += 1  # Increment score when snake eats food

                    self.screen.fill(BLACK)
                    self.snake.draw(self.screen)
                    self.food.draw(self.screen)
                    # Render and draw the score text
                    score_text = self.font.render(f'SCORE: {self.score}', True, (255, 255, 255))
                    self.screen.blit(score_text, (10, 10))
                    pygame.display.flip()
                    self.clock.tick(10)

        pygame.quit()