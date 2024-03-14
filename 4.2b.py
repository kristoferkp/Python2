import operator

fail = open("maalähedane.csv", "r", encoding="UTF-8")

osalejad = {}

for rida in fail:
    osad = rida.split(";")
    maakond = osad[0]
    osad.pop(0)
    osad = [ int(x) for x in osad ]
    osalejad[maakond] = sum(osad)
          
fail.close()

maxKey = max(osalejad.items(), key=operator.itemgetter(1))[0]
maxValue = osalejad.get(maxKey)
kokku = sum(osalejad.values())

print(f'{maxKey} - {maxValue}')
print(f'{kokku}')