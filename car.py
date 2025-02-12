import pygame
import random
import sys

# Pygame boshlang'ich sozlamalari
pygame.init()

# Ekran o‘lchami
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avtomobil O‘yini")

# Ranglar
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# O‘yin elementlari
car_width, car_height = 50, 100
car_x, car_y = WIDTH // 2, HEIGHT - 120
car_speed = 7

obstacle_width, obstacle_height = 50, 100
obstacle_speed = 5
obstacles = []

score = 0
font = pygame.font.SysFont(None, 36)

# Funksiya: Matn chizish
def draw_text(text, x, y, color):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, (x, y))

# Funksiya: To‘siqlarni chizish
def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)

# Funksiya: O‘yinni qayta boshlash
def restart_game():
    global car_x, car_y, obstacles, score, obstacle_speed
    car_x, car_y = WIDTH // 2, HEIGHT - 120
    obstacles = []
    score = 0
    obstacle_speed = 5

# Asosiy tsikl
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    # Eventlarni tekshirish
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Klaviatura nazorati
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
        car_x += car_speed

    # To‘siqlarni yaratish
    if random.randint(1, 30) == 1:
        obstacle_x = random.randint(0, WIDTH - obstacle_width)
        obstacles.append(pygame.Rect(obstacle_x, 0, obstacle_width, obstacle_height))

    # To‘siqlarni harakatlantirish
    for obstacle in obstacles[:]:
        obstacle.y += obstacle_speed
        if obstacle.colliderect(pygame.Rect(car_x, car_y, car_width, car_height)):
            draw_text("GAME OVER!", WIDTH // 3, HEIGHT // 3, RED)
            pygame.display.flip()
            pygame.time.wait(2000)
            restart_game()
        if obstacle.y > HEIGHT:
            obstacles.remove(obstacle)
            score += 1

    # To‘siqlarni chizish
    draw_obstacles()

    # O‘yinchi avtomobilini chizish
    pygame.draw.rect(screen, BLUE, (car_x, car_y, car_width, car_height))

    # Ballarni ko‘rsatish
    draw_text(f"Ball: {score}", 10, 10, BLACK)

    # Tezlikni oshirish
    if score % 10 == 0 and score != 0:
        obstacle_speed += 0.01

    pygame.display.flip()
    clock.tick(60)
