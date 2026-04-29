import pygame
import sys

# 1. PyGame'i initsialiseerimine
pygame.init()

# 2. Akna loomine (laius 640, kõrgus 480)
ekraani_laius = 640
ekraani_korgus = 480
ekraan = pygame.display.set_mode((ekraani_laius, ekraani_korgus))
pygame.display.set_caption("Ülesanne 2")

# 3. Piltide laadimine
# Kasutame transform.scale, et taustapilt kataks kindlasti terve 640x480 akna
taust = pygame.image.load("bgshop.jpg")
taust = pygame.transform.scale(taust, (ekraani_laius, ekraani_korgus))

muuja = pygame.image.load("seller.png")
muuja = pygame.transform.scale(muuja, [265, 314])
jutumull = pygame.image.load("chat.png")

# 4. Teksti seadistamine
# Kasutame Pygame'i vaikimisi fonti (None) ja suurust 32
font = pygame.font.Font(None, 32)
# Tekst "Tere, olen Steven", True tähendab anti-aliasingut (siledad ääred), (255, 255, 255) on valge värv (RGB)
tekst_pilt = font.render("Tere, olen Steven", True, (255, 255, 255))
tekst_pilt2 = font.render("Jürimäe", True, (255, 255, 255))

# 5. Mängu põhitsükkel
tootab = True
while tootab:
    # Sündmuste kontrollimine (nt akna sulgemine ristist)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tootab = False

    # 6. Piltide ekraanile joonistamine (blit)
    # Järjekord on oluline: kõigepealt taust, siis müüja, siis jutumull ja kõige peale tekst.

    # Joonistame tausta koordinaatidele (0, 0) - ülemine vasak nurk
    ekraan.blit(taust, (0, 0))

    # Joonistame müüja (MUÜDA NEID NUMBREID, ET MÜÜJAT LIIGUTADA: (x, y))
    ekraan.blit(muuja, (90, 160))

    # Joonistame jutumulli (MUÜDA NEID NUMBREID: (x, y))
    ekraan.blit(jutumull, (240, 50))

    # Joonistame teksti jutumulli sisse (MUÜDA NEID NUMBREID, et tekst oleks täpselt mulli keskel)
    ekraan.blit(tekst_pilt, (280, 100))
    ekraan.blit(tekst_pilt2, (280, 130))

    # Värskendame ekraani, et muudatused nähtavale ilmuksid
    pygame.display.flip()

# 7. Programmi sulgemine
pygame.quit()
sys.exit()