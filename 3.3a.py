korteriteList = []
def nummerda(korrusteArv, korteriteArv):
    for korrus in range(korrusteArv):
        korteridKorrusel = []
        for i in range(korteriteArv):
            korteridKorrusel.append(str(korrus + 1) + str(i + 1))
            
        korteriteList.append(korteridKorrusel)
    return korteriteList