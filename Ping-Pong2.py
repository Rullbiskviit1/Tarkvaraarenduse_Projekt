import pygame
import sys

# Initsialiseeri Pygame
pygame.init()

# 1. Ekraani seaded
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping-Pong")

# Hele sinine taustavärv (RGB)
LIGHT_BLUE = (173, 216, 230)
BLACK = (0, 0, 0)

# Lae ja muuda piltide suurust
try:
    ball_img = pygame.image.load("ball-1.png").convert_alpha()
    ball_img = pygame.transform.scale(ball_img, (20, 20))  # palli suurus 20x20
except FileNotFoundError:
    print("Viga: Pilti 'ball-1.png' ei leitud!")
    sys.exit()

try:
    pad_img = pygame.image.load("pad.png").convert_alpha()
    pad_img = pygame.transform.scale(pad_img, (120, 20))  # aluse suurus 120x20
except FileNotFoundError:
    print("Viga: Pilti 'pad.png' ei leitud!")
    sys.exit()

# 2. Palli algseaded
ball_rect = ball_img.get_rect()
# Palli alguspunkt
ball_pos_x = -5
ball_pos_y = -5
ball_speed_x = 8.0
ball_speed_y = 8.0

# 3. Aluse algseaded
pad_rect = pad_img.get_rect()
pad_rect.x = WIDTH // 2 - 60
pad_rect.y = HEIGHT / 1.5
pad_speed_x = 7

# 4. Skoori seaded
score = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

# Põhitsükkel
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # --- Mängija sisend (Aluse liigutamine) ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and pad_rect.left > 0:
        pad_rect.x -= pad_speed_x
    if keys[pygame.K_RIGHT] and pad_rect.right < WIDTH:
        pad_rect.x += pad_speed_x

    # --- Palli liigutamine ---
    ball_pos_x += ball_speed_x
    ball_pos_y += ball_speed_y

    ball_rect.x = int(ball_pos_x)
    ball_rect.y = int(ball_pos_y)

    # --- Kokkupõrgete tuvastamine ---

    # Pall põrkub vasakust ja paremast seinast
    if ball_rect.left <= 0 or ball_rect.right >= WIDTH:
        ball_speed_x = -ball_speed_x

    # Pall põrkub ülemisest seinast
    if ball_rect.top <= 0:
        ball_speed_y = -ball_speed_y

    # Pall puudutab alumist äärt (mängija saab negatiivse punkti)
    if ball_rect.bottom >= HEIGHT:
        score -= 1
        ball_speed_y = -ball_speed_y

    # Pall puutub alust
    if ball_rect.colliderect(pad_rect) and ball_speed_y > 0:
        ball_speed_y += 0.2

        if ball_speed_x > 0:
            ball_speed_x += 0.2
        else:
            ball_speed_x -= 0.2

        ball_speed_y = -ball_speed_y
        score += 1

    # --- Joonistamine ---
    screen.fill(LIGHT_BLUE)

    screen.blit(ball_img, ball_rect)
    screen.blit(pad_img, pad_rect)

    score_text = font.render(f"Punkte: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)