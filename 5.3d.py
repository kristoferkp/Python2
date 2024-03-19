def nurkademanguks_vaja(matrix):
    listi = []
    listi.append(matrix[0][0])
    listi.append(matrix[0][4])
    listi.append(matrix[4][0])
    listi.append(matrix[4][4])
    
    vastus = []
    for i in listi:
        if i != "X":
            vastus.append(i)
    return vastus


def diagonaalidemanguks_vaja(matrix):
    listi = []
    listi.append(matrix[0][0])
    listi.append(matrix[1][1])
    listi.append(matrix[2][2])
    listi.append(matrix[3][3])
    listi.append(matrix[4][4])
    
    listi.append(matrix[4][0])
    listi.append(matrix[3][1])
    # listi.append(matrix[2][2])
    listi.append(matrix[1][3])
    listi.append(matrix[0][4])
    
    vastus = []
    for i in listi:
        if i != "X":
            vastus.append(i)
    return vastus
    
    
def taismanguks_vaja(matrix):
    listi = []
    
    for rida in matrix:
        for arv in rida:
            if arv != "X":
                listi.append(arv)
                
    return listi