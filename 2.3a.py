fail = open("retseptid.txt", encoding="UTF-8")

retseptid_tabel = [] # Tühi järjend, kuhu lisame retseptid

for rida in fail:    # Iga rea jaoks failist
    koostisosad = []     # Kogume reas olevad koostisosad järjendisse
    osad = rida.split(",") # Jupitame rea koma koha pealt

    for osa in osad: # Vaatame iga juppi eraldi
        koostisosad.append(osa.strip()) # Lisame reas olevad koostisosad järjendisse

    retseptid_tabel.append(koostisosad) # Lisame koostisosade järjendi retseptide tabelisse

fail.close()

print("Retseptid, milleks on vaja maasikaid ja suhkrut: ")

for retsept in retseptid_tabel:
    if retsept.count('maasikad') > 0 and retsept.count('suhkur') > 0:
        print(retsept)
        
