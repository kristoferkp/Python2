def kooslubajad(erakonnad):
    max_uhisosa = 0
    indeksid = (0, 0)
    for i in range(len(erakonnad)):
        for j in range(i+1, len(erakonnad)):
            uhisosa = len(erakonnad[i].intersection(erakonnad[j]))
            if uhisosa >= max_uhisosa:
                max_uhisosa = uhisosa
                indeksid = (i, j)
    return indeksid