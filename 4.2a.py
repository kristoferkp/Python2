fail = open("tehnika.txt", "r", encoding="UTF-8")

for rida in fail:
    osad = rida.split(" ")
    protsendid = []
    tehnika = osad[0]
    for i in range(1, len(osad)):
        protsendid.append(int(osad[i]))
      
    diff = protsendid[-1] - protsendid[0]
    if diff > 10:
        print(f'{tehnika} - {diff}%')
        
fail.close()