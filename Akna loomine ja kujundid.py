from tkinter import *

# 1. Tekitame uue akna ja määrame suuruse (300x300)
aken = Tk()
aken.geometry("300x300")

# 2. Lisame programmiaknale töönime ja omanime
aken.title("Lumemees – Steven Jürimäe")

# 3. Loome joonistusala (Canvas)
# Valime taustavärviks helesinise (lightblue), et valge lumemees oleks hästi nähtav
tahvel = Canvas(aken, width=300, height=300, bg="lightblue")
tahvel.pack()

# 4. Joonistame objektid (lumemehe 3 palli)
# Koordinaadid on valitud nii, et lumemees täidaks akna mõistlikkuse piires

# Alumine pall (kõige suurem)
tahvel.create_oval(80, 160, 220, 290, fill="white", outline="black")

# Keskmine pall
tahvel.create_oval(100, 70, 200, 170, fill="white", outline="black")

# Ülemine pall (pea)
tahvel.create_oval(115, 10, 185, 80, fill="white", outline="black")

# --- Lisadetailid, et objekt oleks selgelt lumemees ---
# Silmad
tahvel.create_oval(135, 30, 145, 40, fill="black")
tahvel.create_oval(155, 30, 165, 40, fill="black")

# Porgandnina (kolmnurk)
tahvel.create_polygon(150, 45, 150, 55, 175, 50, fill="orange", outline="black")

# Nööbid keskmisele pallile
tahvel.create_oval(145, 90, 155, 100, fill="black")
tahvel.create_oval(145, 115, 155, 125, fill="black")
tahvel.create_oval(145, 140, 155, 150, fill="black")

# Hoiame akent avatuna, kuni kasutaja selle sulgeb
aken.mainloop()