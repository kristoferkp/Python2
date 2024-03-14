fail = open("konto.txt", "r", encoding="UTF-8")

for rida in fail:
    if float(rida) >= 0:
        print(rida)

fail.close()
