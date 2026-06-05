import pygame
import sys

# Initsialiseeri Pygame
pygame.init()

# 1. Ekraani seaded
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Põrkava Palli Mäng")

# Hele sinine taustavärv (RGB)
LIGHT_BLUE = (173, 216, 230)
BLACK = (0, 0, 0)

# Lae ja muuda piltide suurust
# Kasutame try-except plokki, et vältida krahhi, kui pilte ei leita
try:
    ball_img = pygame.image.load("ball-1.png").convert_alpha()
    ball_img = pygame.transform.scale(ball_img, (20, 20))  # palli suurus 20x20
except FileNotFoundError:
    print("Viga: Pilti 'ball-1.png' ei leitud! Asenda see õige failiga.")
    sys.exit()

try:
    pad_img = pygame.image.load("pad.png").convert_alpha()
    pad_img = pygame.transform.scale(pad_img, (120, 20))  # aluse suurus 120x20
except FileNotFoundError:
    print("Viga: Pilti 'pad.png' ei leitud! Asenda see õige failiga.")
    sys.exit()

# 2. Palli algseaded
ball_rect = ball_img.get_rect()
ball_rect.x = WIDTH // 2
ball_rect.y = HEIGHT // 4
ball_speed_x = 4  # palli kiirus x-teljel
ball_speed_y = 4  # palli kiirus y-teljel

# 3. Aluse algseaded
pad_rect = pad_img.get_rect()
pad_rect.x = WIDTH // 2 - 60
pad_rect.y = HEIGHT / 1.5  # aluse y-koordinaat keskkohast allpool
pad_speed_x = 5  # aluse liikumiskiirus

# 4. Skoori seaded (Boonus)
score = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

# Põhitsükkel
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Liiguta palli
    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y

    # Liiguta alust
    pad_rect.x += pad_speed_x

    # --- Kokkupõrgete tuvastamine ---

    # Alus põrkub seintest tagasi
    if pad_rect.left <= 0 or pad_rect.right >= WIDTH:
        pad_speed_x = -pad_speed_x

    # Pall põrkub vasakust ja paremast seinast
    if ball_rect.left <= 0 or ball_rect.right >= WIDTH:
        ball_speed_x = -ball_speed_x

    # Pall põrkub ülemisest seinast
    if ball_rect.top <= 0:
        ball_speed_y = -ball_speed_y

    # Pall puudutab alumist äärt (mängija saab negatiivse punkti)
    if ball_rect.bottom >= HEIGHT:
        score -= 1
        ball_speed_y = -ball_speed_y  # põrkab ka alt tagasi

    # Pall puutub alust (mängija saab positiivse punkti)
    # Kontrollime ka, et pall liigub ülevalt alla (ball_speed_y > 0), et vältida imelikku käitumist
    if ball_rect.colliderect(pad_rect) and ball_speed_y > 0:
        ball_speed_y = -ball_speed_y
        score += 1

    # --- Joonistamine ---

    # Joonista helesinine taust
    screen.fill(LIGHT_BLUE)

    # Joonista pall ja alus
    screen.blit(ball_img, ball_rect)
    screen.blit(pad_img, pad_rect)

    # Joonista skoor ülemisse vasakusse nurka
    score_text = font.render(f"Punkte: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Värskenda ekraani
    pygame.display.flip()

    # Piira kaadrisagedust (60 kaadrit sekundis)
    clock.tick(60)