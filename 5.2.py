failinimi = input("Andmebaasi faili nimi: ")
tahised = input("Piiriületajad: ").split(" ")

def failist_sonastik(failinimi):
    fail = open(failinimi, "r", encoding="UTF-8")
    dictonary = {}
    for rida in fail:
        osad = rida.split(" ")
        dictonary[osad[0]] = osad[1].strip()
    fail.close()
    return dictonary
    
def tahised_nimedeks(tahised, sonastik):
    vastus = [] 
    for element in tahised:
        if element in sonastik.keys():
            vastus.append(sonastik[element])
        else:
            vastus.append(None)
            
    return vastus
    

for e in tahised_nimedeks(tahised, failist_sonastik(failinimi)):
    if e is not None:
        print(e)
    else:
        print("Tundmatu maa")