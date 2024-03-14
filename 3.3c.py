failiNimi = input("Sisestage failinimi: ")

reaNr = 0
maxNr = 0
list = []

fail = open(failiNimi, "r", encoding="UTF-8")

for rida in fail:
    arvudeList = []
    arvud = rida.split()
    
    for arv in arvud:
        arvudeList.append(int(arv))
        print(arv)
        
    list.append(arvudeList)

fail.close()

for arvList in list:
    sumarv = sum(arvList)
    if sumarv > maxNr:
        maxNr = sumarv
        reaNr = list.index(arvList)
        
print(f'Suurim summa on failis {reaNr}. real ja see on {maxNr}')

