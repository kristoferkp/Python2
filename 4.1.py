fail = open("hinded.csv", "r", encoding="UTF-8")

for rida in fail:
    osad = rida.split(",")
    hinded = []
    aine = osad[0]
    for i in range(1, len(osad)):
        hinded.append(int(osad[i]))
        
    keskmine = round(sum(hinded)/len(hinded), 1)
    print(f'{aine}: {keskmine}')