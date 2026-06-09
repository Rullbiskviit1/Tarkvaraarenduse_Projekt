import pygame
import random
import sys

# 1. Pygame'i initsialiseerimine
pygame.init()

# 2. Kasutaja ekraani suuruse tuvastamine
screen_info = pygame.display.Info()
AKNA_LAIUS = screen_info.current_w
AKNA_KÕRGUS = screen_info.current_h - 60

# Akna loomine
screen = pygame.display.set_mode((AKNA_LAIUS, AKNA_KÕRGUS))
pygame.display.set_caption("Ü7")

# 3. Värvid
HELESININE = (154, 204, 255)

# 4. Ringide nimekiri ja algne raadius
ringid = []
hetke_raadius = 10  # Esimene ring alustab 10px raadiusega

# Mängu põhitsükkel
running = True
clock = pygame.time.Clock()

while running:
    # Sündmuste kontroll
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Ainult hiire vasak klikk

                # A. Genereerime uuele ringile suvalise värvi
                suvaline_varv = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                # B. Loome uue ringi kasutades 'hetke_raadius' väärtust
                uus_ring = {
                    'pos': event.pos,
                    'color': suvaline_varv,
                    'radius': hetke_raadius
                }
                ringid.append(uus_ring)

                # C. Kasvatame raadiust JÄRGMISE ringi jaoks 5 piksli võrra
                hetke_raadius += 5

                # D. Kui ringe on üle 10, kustutame kõige vanema
                if len(ringid) > 10:
                    ringid.pop(0)

                if hetke_raadius > AKNA_KÕRGUS / 2:
                    hetke_raadius = 10
                else:
                    hetke_raadius == hetke_raadius

    # 5. Ekraani joonistamine
    screen.fill(HELESININE)

    # Kõigi nimekirjas olevate ringide joonistamine
    for ring in ringid:
        # Viimane number '3' määrab joone paksuse, jättes ringi seest tühjaks
        pygame.draw.circle(screen, ring['color'], ring['pos'], ring['radius'], 3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()