from tkinter import *

# 1. Akna loomine ja seadistamine
aken = Tk()
aken.geometry("300x300")
aken.title("Lumemees – Steven Jürimäe")

# Tahvli loomine (taust helesinine)
tahvel = Canvas(aken, width=300, height=300, bg="lightblue")
tahvel.pack()

# TAUSTA OBJEKTID (Joonistame kõigepealt)

# Päikeseketas
tahvel.create_oval(15, 15, 65, 65, fill="yellow", outline="gold")

# Põhisuunad (üles, alla, vasakule, paremale)
tahvel.create_line(40, 10, 40, 0, fill="gold", width=3)           # Kiir üles (UUS)
tahvel.create_line(40, 70, 40, 85, fill="gold", width=3)          # Kiir alla
tahvel.create_line(10, 40, 0, 40, fill="gold", width=3)           # Kiir vasakule (UUS)
tahvel.create_line(70, 40, 85, 40, fill="gold", width=3)          # Kiir paremale

# Diagonaalsed suunad
tahvel.create_line(20, 20, 5, 5, fill="gold", width=3)            # Kiir üles-vasakule (UUS)
tahvel.create_line(60, 20, 75, 5, fill="gold", width=3)           # Kiir üles-paremale
tahvel.create_line(20, 60, 5, 75, fill="gold", width=3)           # Kiir alla-vasakule
tahvel.create_line(60, 60, 75, 75, fill="gold", width=3)          # Kiir alla-paremale

# 5. Kolm pilve (koosnevad mitmest ülekattega ringist)
# Pilv 1 (üleval paremal)
tahvel.create_oval(190, 20, 230, 40, fill="white", outline="white")
tahvel.create_oval(210, 10, 250, 35, fill="white", outline="white")
tahvel.create_oval(230, 20, 270, 40, fill="white", outline="white")

# Pilv 2 (keskel vasakul, päikese all)
tahvel.create_oval(10, 110, 40, 130, fill="white", outline="white")
tahvel.create_oval(25, 100, 60, 125, fill="white", outline="white")
tahvel.create_oval(45, 110, 75, 130, fill="white", outline="white")

# Pilv 3 (keskel paremal)
tahvel.create_oval(220, 90, 250, 110, fill="white", outline="white")
tahvel.create_oval(235, 80, 270, 105, fill="white", outline="white")
tahvel.create_oval(255, 90, 285, 110, fill="white", outline="white")

# LUMEMEHE TAGUMISED DETAILID

# 1. Käed (pruunid jooned)
# Vasak käsi
tahvel.create_line(120, 150, 60, 130, width=4, fill="saddlebrown")
# Parem käsi
tahvel.create_line(180, 150, 240, 130, width=4, fill="saddlebrown")

# 3. Kätte hari (paremasse kätte)
# Luuavars
tahvel.create_line(230, 230, 250, 70, width=3, fill="saddlebrown")
# Luuaots (harjased) - kolmnurk
tahvel.create_polygon(250, 70, 235, 30, 265, 30, fill="khaki", outline="saddlebrown")

# LUMEMEHE KEHA

# Nihutatud veidi allapoole, et kübar ära mahuks
# Alumine pall
tahvel.create_oval(80, 190, 220, 290, fill="white", outline="black")
# Keskmine pall
tahvel.create_oval(100, 100, 200, 200, fill="white", outline="black")
# Ülemine pall (pea)
tahvel.create_oval(115, 40, 185, 110, fill="white", outline="black")

# LUMEMEHE ESIMESED DETAILID

# 2. Kübar (koosneb kahest ristkülikust)
# Kübara äär
tahvel.create_rectangle(105, 35, 195, 45, fill="black")
# Kübara ülemine toru
tahvel.create_rectangle(125, 5, 175, 35, fill="black")

# Silmad
tahvel.create_oval(135, 60, 145, 70, fill="black")
tahvel.create_oval(155, 60, 165, 70, fill="black")

# Porgandnina
tahvel.create_polygon(150, 75, 150, 85, 175, 80, fill="orange", outline="black")

# Nööbid keskmisele pallile
tahvel.create_oval(145, 120, 155, 130, fill="black")
tahvel.create_oval(145, 145, 155, 155, fill="black")
tahvel.create_oval(145, 170, 155, 180, fill="black")

# Programmi töös hoidmine
aken.mainloop()