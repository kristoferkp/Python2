def kooslubajad(erakonnad):
    dictonary = {}
    for erakond in erakonnad:
        lubadused = []
        for lubadus in erakond:
            lubadused.append(lubadus)
        dictonary[erakonnad.index(erakond)] = lubadused
        
print(kooslubajad([{"maamaks kaotada", "pensione tõsta", "kaitsekulutusi tõsta"},
                 {"lasteaiaõpetajate palku tõsta", "kindlustada tasuta hambaravi kuni 30-aastastele"},
                 {"sisserännet piirata", "pensione tõsta", "kaitsekulutusi tõsta"},
                 set()]))