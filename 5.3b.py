from random import sample

def juhuslik_bingo():
    matrix = []
    veerg1 = sample(range(1, 16), 5)
    veerg2 = sample(range(16, 31), 5)
    veerg3 = sample(range(31, 46), 5)
    veerg4 = sample(range(46, 61), 5)
    veerg5 = sample(range(61, 76), 5)
    
    for i in range(0, 4):
        matrix.append([veerg1[i], veerg2[i], veerg3[i], veerg4[i], veerg5[i],])
    
    return matrix