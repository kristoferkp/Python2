fail = open("kalorid.txt", encoding="UTF-8")

toitude_tabel = []

for rida in fail: # iga rea jaoks failist
    korra_grammid = [] # kogume ühe toidukorra info
    osad = rida.split() # tühikute kohalt osadeks

    for osa in osad: # osade kaupa
        korra_grammid.append(int(osa)) # järjekordne info juurde

    toitude_tabel.append(korra_grammid) # toidukorra järjend juurde

fail.close()

kokku = 0

for toit in toitude_tabel:
    kokku += toit[0] * 4
    kokku += toit[1] * 4
    kokku += toit[2] * 9

print(kokku)