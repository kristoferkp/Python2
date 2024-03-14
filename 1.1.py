def kala_kaal(pikkus, indeks):
    return round(pikkus**3 * indeks / 100)

failiNimi = input("Sisesta faili nimi: ")
alam = float(input("Mis on püügi alammõõt? "))
indeks = float(input("Sisesta Fultoni tüsedusindeks: "))

file = open(failiNimi, "r", encoding="UTF-8")
suurim = 0

for i in file:
    i = int(i)
    kaal = kala_kaal(i, indeks)
    if i <= alam:
        print("Kala lasti vette tagasi")
    if kaal > suurim:
        suurim = kaal
    print(f'Püütud kala kaaluga {kaal} grammi')
    
print(f'Kõige raskem püütud kala: {suurim / 1000} kg')