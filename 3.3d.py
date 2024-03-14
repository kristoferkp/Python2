
def voitis_nurkademangu(matrix):
    if matrix[0][0] == "X" and matrix[0][4] == "X" and matrix[4][0] == "X" and matrix[4][4] == "X":
        return True
    else:
        return False
    
def voitis_diagonaalidemangu(matrix):
    if x_peadiagonaalil(matrix) == 5 and x_korvaldiagonaalil(matrix) == 5:
        return True
    else:
        return False
        
def x_peadiagonaalil(matrix):
    dia =[ matrix[0][0], matrix[1][1], matrix[2][2], matrix[3][3], matrix[4][4]]
    return dia.count("X")
    
def x_korvaldiagonaalil(matrix):
    dia =[ matrix[4][0], matrix[3][1], matrix[2][2], matrix[1][3], matrix[0][4]]
    return dia.count("X")

def voitis_taismangu(matrix):
    tais = True
    for i in matrix:
        if i.count("X") != 5:
            tais = False
    return tais