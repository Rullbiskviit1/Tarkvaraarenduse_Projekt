import pygame
import sys

# 1. Initsialiseerime PyGame'i ja tekitame uue akna (300x300)
pygame.init()
aken = pygame.display.set_mode((300, 300))

# 2. Lisame programmiaknale töönime ja omanime
pygame.display.set_caption("Lumemees – Steven Jürimäe")

# Värvide definitsioonid (RGB-vormingus)
HELESINIHE = (173, 216, 230)
VALGE = (255, 255, 255)
MUST = (0, 0, 0)
ORANZ = (255, 165, 0)

# Kell mängukiiruse (FPS) juhtimiseks
kell = pygame.time.Clock()

# Programmi põhitsükkel
running = True
while running:
    # Kontrollime sündmusi (et aken sulguks ristist vajutades)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. Valime taustavärviks helesinise
    aken.fill(HELESINIHE)

    # 4. Joonistame objektid (lumemehe 3 palli)
    # PyGame kasutab vormingut: [x, y, laius, kõrgus]

    # Alumine pall (kõige suurem)
    pygame.draw.ellipse(aken, VALGE, [80, 160, 140, 130])
    pygame.draw.ellipse(aken, MUST, [80, 160, 140, 130], 1)  # Must äär

    # Keskmine pall
    pygame.draw.ellipse(aken, VALGE, [100, 70, 100, 100])
    pygame.draw.ellipse(aken, MUST, [100, 70, 100, 100], 1)

    # Ülemine pall (pea)
    pygame.draw.ellipse(aken, VALGE, [115, 10, 70, 70])
    pygame.draw.ellipse(aken, MUST, [115, 10, 70, 70], 1)

    # --- Lisadetailid ---
    # Silmad
    pygame.draw.ellipse(aken, MUST, [135, 30, 10, 10])
    pygame.draw.ellipse(aken, MUST, [155, 30, 10, 10])

    # Porgandnina (kolmnurk)
    pygame.draw.polygon(aken, ORANZ, [(150, 45), (150, 55), (175, 50)])
    pygame.draw.polygon(aken, MUST, [(150, 45), (150, 55), (175, 50)], 1)

    # Nööbid keskmisele pallile
    pygame.draw.ellipse(aken, MUST, [145, 90, 10, 10])
    pygame.draw.ellipse(aken, MUST, [145, 115, 10, 10])
    pygame.draw.ellipse(aken, MUST, [145, 140, 10, 10])

    # Uuendame ekraani graafikat
    pygame.display.flip()

    # Piirame tsükli kiirust (60 kaadrit sekundis)
    kell.tick(60)

# Sulgeme PyGame'i puhtalt, kui tsükkel lõppeb
pygame.quit()
sys.exit()