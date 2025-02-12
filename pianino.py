import pygame
import sys
import random
import os
import urllib.request

# Pygame boshlash
pygame.init()

# Ekran parametrlari
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pianino O'yini")

# Ranglar
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Klaviatura tugmalari
keys = ["A", "S", "D", "F"]
key_positions = [50, 150, 250, 350]  # Tugmalar koordinatalari

# Notalar
notes = []
note_speed = 5

# Ball
score = 0
font = pygame.font.Font(None, 36)

# Ovozlarni yuklash yoki yuklab olish
pygame.mixer.init()
sound_paths = [f"note{i}.wav" for i in range(1, 5)]
sound_urls = [
    "https://www.soundjay.com/button/beep-01a.wav",
    "https://www.soundjay.com/button/beep-02.wav",
    "https://www.soundjay.com/button/beep-03.wav",
    "https://www.soundjay.com/button/beep-04.wav"
]

def download_sounds():
    for i, path in enumerate(sound_paths):
        if not os.path.exists(path):
            print(f"Yuklanmoqda: {path}")
            urllib.request.urlretrieve(sound_urls[i], path)
            print(f"Yuklandi: {path}")

try:
    # Agar ovozlar mavjud bo'lmasa yuklab olamiz
    download_sounds()
    sounds = [pygame.mixer.Sound(path) for path in sound_paths]
except Exception as e:
    print(f"Ovozlarni yuklashda xatolik: {e}")
    sounds = [None] * 4

# Asosiy o'yin tsikli
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    # Tadbirlarni tekshirish
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN:
            for i, key in enumerate(keys):
                if event.unicode.upper() == key:
                    if notes and notes[0][0] == key_positions[i]:
                        score += 10
                        if sounds[i]:
                            sounds[i].play()
                        notes.pop(0)
                    else:
                        score -= 5

    # Yangi nota yaratish
    if random.randint(1, 30) == 1:
        notes.append([random.choice(key_positions), 0])

    # Notalarni yangilash
    for note in notes:
        note[1] += note_speed
        pygame.draw.rect(screen, GRAY, (note[0], note[1], 50, 20))
    notes = [note for note in notes if note[1] < HEIGHT]

    # Tugmalarni chizish
    for i, x in enumerate(key_positions):
        pygame.draw.rect(screen, BLACK, (x, HEIGHT - 50, 50, 50))
        text = font.render(keys[i], True, WHITE)
        screen.blit(text, (x + 15, HEIGHT - 40))

    # Ballni ko'rsatish
    score_text = font.render(f"Ball: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # O'yinni tugatish shartlari
    if score < 0:
        running = False
        print("O'yin tugadi! Yakuniy ball:", score)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
