import pygame
import random

# Pygame ni boshlash
pygame.init()

# O'yin ekranini sozlash
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platforma O'yini")

# Ranglar
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# O'yinchi xususiyatlari
player_width = 50
player_height = 50
player_x = 100
player_y = screen_height - player_height - 10
player_velocity = 5

# Platformalar
platforms = [(0, screen_height - 40, screen_width, 40)]  # Pastki platforma
platform_width = 100
platform_height = 10

# O'yin oynasining yangilanishi
clock = pygame.time.Clock()

# O'yin boshqaruvi
is_jumping = False
jump_count = 10

def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, player_width, player_height))

def draw_platforms():
    for platform in platforms:
        pygame.draw.rect(screen, GREEN, platform)

def move_player(x, y):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= player_velocity
    if keys[pygame.K_RIGHT]:
        x += player_velocity
    return x, y

def jump(y, is_jumping, jump_count):
    if is_jumping:
        y -= jump_count
        jump_count -= 1
        if jump_count < -10:
            is_jumping = False
            jump_count = 10
    else:
        if y < screen_height - player_height - 10:
            y += 10
        else:
            is_jumping = False
    return y, is_jumping, jump_count

# O'yin boshqaruvi
running = True
while running:
    screen.fill(WHITE)
    draw_platforms()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # O'yinchi harakatini boshqarish
    player_x, player_y = move_player(player_x, player_y)

    # Sakrash harakati
    player_y, is_jumping, jump_count = jump(player_y, is_jumping, jump_count)

    draw_player(player_x, player_y)

    pygame.display.update()
    clock.tick(30)  # FPS

pygame.quit()
