fail = open("tulemused.txt", encoding="UTF-8")

tulemuste_tabel = []

for rida in fail:
    seti_punktid = []
    osad = rida.split()

    for osa in osad:
        seti_punktid.append(int(osa))

    tulemuste_tabel.append(seti_punktid)
fail.close()

punktid1 = 0
punktid2 = 0

for tulemus in tulemuste_tabel:
    if tulemus[0] > tulemus[1]:
        punktid1 += 1
    elif tulemus[1] > tulemus[0]:
        punktid2 += 1

if punktid1 > punktid2:
    print(f'Eesti võitis {punktid1}-{punktid2}')
elif punktid2 > punktid1:
    print(f'Soome võitis {punktid2}-{punktid1}')