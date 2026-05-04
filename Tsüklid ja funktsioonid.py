import pygame
import threading
import sys

# --- Globaalsed algseaded ---
ekraani_laius = 640
ekraani_korgus = 480
# Lubatud suurused, mis jaguvad täpselt nii 640 kui 480-ga
lubatud_suurused = [1, 2, 4, 5, 8, 10, 16, 20, 32, 40, 80, 160]

samm = 40  # Ruudu laius ja kõrgus (alguses 40x40)
joone_varv = (255, 0, 0)


def leia_lahim_suurus(soovitud_suurus):
    """
    Leiab kasutaja sisestatud numbrile lähima lubatud ruudu suuruse,
    mis katab ekraani ilma poolikute ruutudeta.
    """
    return min(lubatud_suurused, key=lambda x: abs(x - soovitud_suurus))


def joonista_ruudustik(ekraan, laius, korgus, ruudu_suurus, varv):
    """
    Joonistab ruudustiku. Kuna ruudu_suurus sobib ideaalselt ekraaniga,
    tulevad ruudud täpsed ja ilma poolikute äärteta.
    """
    # Horisontaalsed jooned
    for i in range((korgus // ruudu_suurus) + 1):
        y = i * ruudu_suurus
        pygame.draw.line(ekraan, varv, (0, y), (laius, y))

    # Vertikaalsed jooned
    for i in range((laius // ruudu_suurus) + 1):
        x = i * ruudu_suurus
        pygame.draw.line(ekraan, varv, (x, 0), (x, korgus))


def konsooli_kuulaja():
    global samm, joone_varv

    varvid = {
        '1': (255, 0, 0),  # Punane
        '2': (0, 0, 255),  # Sinine
        '3': (255, 165, 0),  # Oranž
        '4': (255, 192, 203),  # Roosa
        '5': (128, 0, 128),  # Lilla
        '6': (255, 255, 0)  # Kollane
    }

    while True:
        try:
            valik = input("\nMida soovite muuta? (s = ruudu suurus, r = ridade arv, v = värv): ").strip().lower()

            if valik == 's':
                uus_suurus = float(input("Sisesta soovitud ruudu suurus: "))
                if uus_suurus > 0:
                    samm = leia_lahim_suurus(uus_suurus)
                    read = ekraani_korgus // samm
                    veerud = ekraani_laius // samm
                    print(f"=> Kohandati: Ruudu suurus on nüüd {samm}. Ekraanil on {read} rida ja {veerud} veergu.")
                else:
                    print("=> Viga: Suurus peab olema nullist suurem.")

            elif valik == 'r':
                soovitud_read = int(input("Sisesta soovitud ridade arv: "))
                if soovitud_read > 0:
                    # Arvutame teoreetilise ruudu suuruse selle ridade arvu jaoks
                    teoreetiline_suurus = ekraani_korgus / soovitud_read
                    # Leiame lähima sobiva suuruse, mis ei tekita poolikuid ruute
                    samm = leia_lahim_suurus(teoreetiline_suurus)
                    tegelik_read = ekraani_korgus // samm
                    tegelik_veerud = ekraani_laius // samm
                    print(
                        f"=> Kohandati: Lähim ideaalne ridade arv on {tegelik_read} (ja {tegelik_veerud} veergu). Ruudu suurus: {samm}.")
                else:
                    print("=> Viga: Arv peab olema nullist suurem.")

            elif valik == 'v':
                print("Vali värv:\n1. punane\n2. sinine\n3. oranž\n4. roosa\n5. lilla\n6. kollane")
                varvi_valik = input("Sisesta number (1-6): ").strip()
                if varvi_valik in varvid:
                    joone_varv = varvid[varvi_valik]
                    print("=> Värv uuendatud!")
                else:
                    print("=> Viga: Sellist numbrit pole valikus.")

            else:
                print("=> Tundmatu valik! Palun sisesta 's', 'r' või 'v'.")

        except ValueError:
            print("=> Viga: Palun sisesta korrektne number!")
        except EOFError:
            break


def main():
    pygame.init()
    ekraan = pygame.display.set_mode((ekraani_laius, ekraani_korgus))
    pygame.display.set_caption("Täiuslik Ruudustik")
    kell = pygame.time.Clock()

    sisendi_loim = threading.Thread(target=konsooli_kuulaja, daemon=True)
    sisendi_loim.start()

    tootab = True
    while tootab:
        for syndmus in pygame.event.get():
            if syndmus.type == pygame.QUIT:
                tootab = False

        ekraan.fill((153, 255, 153))

        joonista_ruudustik(ekraan, ekraani_laius, ekraani_korgus, samm, joone_varv)

        pygame.display.flip()
        kell.tick(30)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()