import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Настройки цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# FPS
clock = pygame.time.Clock()
fps = 60

# Параметры объектов
paddle_width, paddle_height = 100, 20
ball_size = 20
brick_width, brick_height = 75, 30


# Классы объектов
class Paddle:
    def __init__(self):
        self.x = (screen_width - paddle_width) / 2
        self.y = screen_height - paddle_height - 10
        self.width = paddle_width
        self.height = paddle_height
        self.speed = 10

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))

    def move(self, direction):
        if direction == 'left' and self.x > 0:
            self.x -= self.speed
        if direction == 'right' and self.x < screen_width - self.width:
            self.x += self.speed


class Ball:
    def __init__(self):
        self.x = screen_width / 2
        self.y = screen_height / 2
        self.size = ball_size
        self.speed_x = 4 * random.choice([-1, 1])
        self.speed_y = 4
        self.radius = ball_size / 2

    def draw(self):
        pygame.draw.circle(screen, BLUE, (int(self.x), int(self.y)), self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x <= 0 or self.x >= screen_width:
            self.speed_x *= -1
        if self.y <= 0:
            self.speed_y *= -1
        if self.y >= screen_height:
            self.reset()

    def reset(self):
        self.x = screen_width / 2
        self.y = screen_height / 2
        self.speed_x = 4 * random.choice([-1, 1])
        self.speed_y = 4


class Brick:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = brick_width
        self.height = brick_height

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))


# Создание объектов
paddle = Paddle()
ball = Ball()
bricks = [Brick(x * brick_width, y * brick_height + 50) for y in range(3) for x in range(screen_width // brick_width)]

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move('left')
    if keys[pygame.K_RIGHT]:
        paddle.move('right')

    ball.move()

    # Проверка столкновений мяча с ракеткой
    if (paddle.x < ball.x < paddle.x + paddle.width) and (paddle.y < ball.y < paddle.y + paddle.height):
        ball.speed_y *= -1

    # Проверка столкновений мяча с кирпичиками
    bricks_to_remove = []
    for brick in bricks:
        if (brick.x < ball.x < brick.x + brick.width) and (brick.y < ball.y < brick.y + brick.height):
            ball.speed_y *= -1
            bricks_to_remove.append(brick)
    for brick in bricks_to_remove:
        bricks.remove(brick)

    screen.fill(BLACK)
    paddle.draw()
    ball.draw()
    for brick in bricks:
        brick.draw()
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit()