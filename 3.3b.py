def on_bingo_tabel(matrix):
    good = 0
    for rida in matrix:
        if rida[0] >= 1 and rida[0] <= 15 and rida[1] >= 16 and rida[1] <= 30 and rida[2] >= 31 and rida[2] <= 45 and rida[3] >= 46 and rida[3] <= 60 and rida[4] >= 61 and rida[4] <= 75:
            good += 1
    if good == 5:
        return True
    else:
        return False
    
