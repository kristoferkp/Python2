list = []

def vahimatest_suurim(matrix):
    for element in matrix:
        list.append(min(element))
    return max(list)