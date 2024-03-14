list = []

def keskmised(hinnete_tabel):
    for aine in hinnete_tabel:
        nimetus = aine[0]
        aine.pop(0)
        keskmine = round(sum(aine) / len(aine),1)
        list.append([nimetus, keskmine])
    return list
       
