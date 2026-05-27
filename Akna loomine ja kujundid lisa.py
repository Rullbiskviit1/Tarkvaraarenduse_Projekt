import pygame

# 1. Initsialiseerime PyGame'i ja tekitame akna
pygame.init()
aken = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Lumemees – Steven Jürimäe")

# Värvid (RGB)
HELESINIHE = (173, 216, 230)
KOLLANE = (255, 255, 0)
KULDNE = (255, 215, 0)
VALGE = (255, 255, 255)
MUST = (0, 0, 0)
PRUUN = (139, 69, 19)
KHAKI = (240, 230, 140)
ORANZ = (255, 165, 0)

kell = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tausta täitmine
    aken.fill(HELESINIHE)

    # --- TAUSTA OBJEKTID ---
    # Päike
    pygame.draw.ellipse(aken, KOLLANE, [15, 15, 50, 50])
    pygame.draw.ellipse(aken, KULDNE, [15, 15, 50, 50], 2)

    # Päikesekiired
    kiired = [
        ((40, 10), (40, 0)),  # Üles
        ((40, 70), (40, 85)),  # Alla
        ((10, 40), (0, 40)),  # Vasakule
        ((70, 40), (85, 40)),  # Paremale
        ((20, 20), (5, 5)),  # Üles-vasak
        ((60, 20), (75, 5)),  # Üles-parem
        ((20, 60), (5, 75)),  # Alla-vasak
        ((60, 60), (75, 75))  # Alla-parem
    ]
    for algus, lopp in kiired:
        pygame.draw.line(aken, KULDNE, algus, lopp, 3)


    # Pilved (koosnevad mitmest ellipsist)
    def joonista_pilv(x, y):
        pygame.draw.ellipse(aken, VALGE, [x, y + 10, 40, 20])
        pygame.draw.ellipse(aken, VALGE, [x + 20, y, 40, 25])
        pygame.draw.ellipse(aken, VALGE, [x + 40, y + 10, 40, 20])


    joonista_pilv(190, 10)  # Pilv 1
    joonista_pilv(10, 100)  # Pilv 2
    joonista_pilv(220, 80)  # Pilv 3

    # --- LUMEMEHE TAGUMISED DETAILID ---
    # Käed
    pygame.draw.line(aken, PRUUN, (120, 150), (60, 130), 4)
    pygame.draw.line(aken, PRUUN, (180, 150), (240, 130), 4)

    # Hari/Luud
    pygame.draw.line(aken, PRUUN, (230, 230), (250, 70), 3)
    pygame.draw.polygon(aken, KHAKI, [(250, 70), (235, 30), (265, 30)])
    pygame.draw.polygon(aken, PRUUN, [(250, 70), (235, 30), (265, 30)], 1)

    # --- LUMEMEHE KEHA ---
    # Alumine pall
    pygame.draw.ellipse(aken, VALGE, [80, 190, 140, 100])
    pygame.draw.ellipse(aken, MUST, [80, 190, 140, 100], 1)
    # Keskmine pall
    pygame.draw.ellipse(aken, VALGE, [100, 100, 100, 100])
    pygame.draw.ellipse(aken, MUST, [100, 100, 100, 100], 1)
    # Pea
    pygame.draw.ellipse(aken, VALGE, [115, 40, 70, 70])
    pygame.draw.ellipse(aken, MUST, [115, 40, 70, 70], 1)

    # --- KÜBAR ---
    pygame.draw.rect(aken, MUST, [105, 35, 90, 10])  # Äär
    pygame.draw.rect(aken, MUST, [125, 5, 50, 30])  # Toru

    # --- NÄGU JA NÖÖBID ---
    # Silmad
    pygame.draw.ellipse(aken, MUST, [135, 60, 10, 10])
    pygame.draw.ellipse(aken, MUST, [155, 60, 10, 10])
    # Nina
    pygame.draw.polygon(aken, ORANZ, [(150, 75), (150, 85), (175, 80)])
    pygame.draw.polygon(aken, MUST, [(150, 75), (150, 85), (175, 80)], 1)
    # Nööbid
    for y in [120, 145, 170]:
        pygame.draw.ellipse(aken, MUST, [145, y, 10, 10])

    pygame.display.flip()
    kell.tick(60)

pygame.quit()