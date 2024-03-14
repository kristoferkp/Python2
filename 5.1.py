def symbolite_sagedus(sone):
    sonastik = {}
    listi = list(sone)
    for i in range(len(listi)):
        if listi[i] not in sonastik.keys():
            sonastik[listi[i]] = listi.count(listi[i])
    
    return sonastik