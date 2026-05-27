import pygame, sys

pygame.init()

# värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(lBlue)
clock = pygame.time.Clock()

# TÕSTETUD: graafika laadimine ja muutujad peavad olema ENNE tsüklit
ball = pygame.image.load("ball.png")

# kiirus ja asukoht
posX, posY = 0, 0
speedX, speedY = 3, 4

gameover = False
while not gameover:
    # fps
    clock.tick(60)

    # PARANDATUD: küsime evente ainult ühe korra
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()  # Sulgeb Pygame'i korrektselt
            sys.exit()

    # pildi lisamine ekraanile
    screen.blit(ball, (posX, posY))

    # asukoha muutmine
    posX += speedX
    posY += speedY

    # kui puudub ääri, siis muudab suunda
    if posX > screenX - ball.get_rect().width or posX < 0:
        speedX = -speedX

    if posY > screenY - ball.get_rect().height or posY < 0:
        speedY = -speedY

    # graafika kuvamine ekraanil
    pygame.display.flip()
    # Puhastab eelmise kaadri, et pall ei jätaks jälge
    screen.fill(lBlue)