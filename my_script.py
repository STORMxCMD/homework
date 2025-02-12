import pygame
import random

# Pygame dasturini boshlash
pygame.init()

# Ekran o‘lchamini belgilash
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Yomg'ir Tomchilari")

# Ranglar
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Yomg'ir tomchilari sinfi
class Raindrop:
    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(-20, 600)
        self.speed = random.randint(5, 10)
    
    def fall(self):
        self.y += self.speed
        if self.y > 600:
            self.y = random.randint(-20, -1)
            self.x = random.randint(0, 800)

    def draw(self):
        pygame.draw.line(screen, WHITE, (self.x, self.y), (self.x, self.y + 10), 2)

# Yomg'ir tomchilari ro‘yxati
raindrops = [Raindrop() for _ in range(100)]

# Asosiy tsikl
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK)
    
    for drop in raindrops:
        drop.fall()
        drop.draw()
    
    pygame.display.update()
    pygame.time.delay(30)

pygame.quit()
