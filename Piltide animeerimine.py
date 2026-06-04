import pygame
import random

# Initsialiseerime Pygame'i
pygame.init()

# Akna seaded (640x480)
laius = 640
kõrgus = 480
ekraan = pygame.display.set_mode((laius, kõrgus))
pygame.display.set_caption("Ralli Mäng - Pööratud Sinised Autod")

# Piltide laadimine
taust = pygame.image.load("bg_rally.jpg")
punane_auto = pygame.image.load("f1_red.png")
sinine_auto_algne = pygame.image.load("f1_blue.png")

# --- SINISED AUTOD: PÖÖRAMINE ---
# Pöörame algset sinist autot 180 kraadi, et selle nina oleks allapoole.
# Pygame'i pööramine toimub vastupäeva, nii et 180 kraadi pöörab selle "põhjalikuks".
sinine_auto = pygame.transform.rotate(sinine_auto_algne, 180)

# --- SÕIDURAJAD ---
# Määrame kolme sõiduraja keskkohad (x-koordinaadid).
# Vajadusel saad neid arve veidi muuta, et need sobituksid täpselt sinu taustapildi joontega.
rajad = [210, 320, 430]

# --- PUNANE AUTO ---
punane_laius = punane_auto.get_width()
punane_kõrgus = punane_auto.get_height()
# Asetame alguses keskmisele rajale (indeks 1)
punane_x = rajad[1] - punane_laius // 2
punane_y = kõrgus - punane_kõrgus - 10
punane_kiirus = 5 # Punase auto liikumiskiirus vasakule/paremale

# --- SINISED AUTOD ---
sinised_autod = []
# Kasutame nüüd uut, pööratud auto suurust
sinine_laius = sinine_auto.get_width()

# Loome iga raja jaoks ühe sinise auto
for i in range(len(rajad)):
    x = rajad[i] - sinine_laius // 2 # Auto paigutatakse raja keskele
    y = random.randint(-600, -100)   # Erinevad stardikõrgused, et nad ei ilmuks samal ajal
    kiirus = random.randint(3, 6)
    sinised_autod.append([x, y, kiirus])

# --- SKOOR ---
skoor = 0
font = pygame.font.SysFont(None, 36)

# Mängutsükli muutujad
kell = pygame.time.Clock()
mang_kaib = True

while mang_kaib:
    # 1. Sündmuste kontroll
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mang_kaib = False

    # 2. Punase auto liigutamise loogika (klahvivajutused)
    klahvid = pygame.key.get_pressed()
    if klahvid[pygame.K_LEFT]:
        punane_x -= punane_kiirus
    if klahvid[pygame.K_RIGHT]:
        punane_x += punane_kiirus

    # (Valikuline) Piirame punase auto liikumist, et see ei sõidaks ekraanilt välja
    if punane_x < 150:
        punane_x = 150
    if punane_x > 490 - punane_laius:
        punane_x = 490 - punane_laius

    # 3. Taustapildi kuvamine
    ekraan.blit(taust, (0, 0))

    # 4. Siniste autode loogika ja joonistamine
    for auto in sinised_autod:
        auto[1] += auto[2] # Auto liigub y-teljel alla (suureneb koordinaat)

        # Kui auto jõuab alla, viime selle tagasi üles
        if auto[1] > kõrgus:
            auto[1] = random.randint(-400, -50)
            auto[2] = random.randint(3, 6)
            skoor += 1

        # Joonistame pööratud auto. (auto[0], auto[1]) on endiselt selle vasak ülanurk,
        # aga kuna pilt on pööratud 180 kraadi, on selle nina suunatud "põhjapoole".
        ekraan.blit(sinine_auto, (auto[0], auto[1]))

    # 5. Punase auto joonistamine
    ekraan.blit(punane_auto, (punane_x, punane_y))

    # 6. Skoori kuvamine
    skoor_tekst = font.render("Skoor: " + str(skoor), True, (255, 255, 255))
    ekraan.blit(skoor_tekst, (10, 10))

    # 7. Ekraani uuendamine
    pygame.display.flip()
    kell.tick(60)

pygame.quit()