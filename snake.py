import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Размеры блока и скорость змейки
BLOCK_SIZE = 20
SPEED = 10

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Змейка")

# Класс змейки
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x*BLOCK_SIZE)) % SCREEN_WIDTH), (cur[1] + (y*BLOCK_SIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, BLACK, r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)

# Класс еды
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                          random.randint(0, SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, BLACK, r, 1)

# Направления движения
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def main():
    clock = pygame.time.Clock()
    screen.fill(WHITE)

    snake = Snake()
    food = Food()

    while True:
        screen.fill(WHITE)
        snake.handle_keys()
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            food.randomize_position()

        snake.draw(screen)
        food.draw(screen)
        pygame.display.update()
        clock.tick(SPEED)

if __name__ == '__main__':
    main()