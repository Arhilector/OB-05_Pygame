import pygame
import time

# инициализация Pygame
pygame.init()

# создание окна
window_size = 800, 600
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Игра Дяди Джуса")

# загрузка изображений
image = pygame.image.load("sharik.png")
image_rect = image.get_rect()

image2 = pygame.image.load("image2.png")
image_rect2 = image2.get_rect()

# начальные настройки
speed = 5
collision = False

# основной цикл программы
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect.x = mouseX - image_rect.width // 2
            image_rect.y = mouseY - image_rect.height // 2

    # проверка столкновений
    if image_rect.colliderect(image_rect2):
        print("Столкновение!")
        collision = True
    else:
        collision = False

    # обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        image_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        image_rect.x += speed
    if keys[pygame.K_UP]:
        image_rect.y -= speed
    if keys[pygame.K_DOWN]:
        image_rect.y += speed

    # заполнение экрана и отрисовка объектов
    screen.fill((0, 0, 0))
    screen.blit(image, image_rect)
    screen.blit(image2, image_rect2)

    # обновление дисплея
    pygame.display.flip()

# выход из Pygame
pygame.quit()





