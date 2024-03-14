def sorteeri(failinimi):
    with open(failinimi, "r") as fail:
        albumid = []
        for rida in fail:
            osad = rida.strip().split(";")
            albumid.append(osad)
            
    albumid_aastakumnete_kaupa = {}
    for album in albumid:
        aasta = int(album[2])
        aastakymne = aasta // 10 * 10
        if aastakymne not in albumid_aastakumnete_kaupa:
            albumid_aastakumnete_kaupa[aastakymne] = []
        albumid_aastakumnete_kaupa[aastakymne].append(album)

    return albumid_aastakumnete_kaupa

def kuva(albumid_aastakumnete_kaupa):
    for aastakymne, albumid in sorted(albumid_aastakumnete_kaupa.items()):
        albumite_arv = len(albumid)
        enim_myydud_album = max(albumid, key=lambda x: int(x[3]))
        artist, albumi_nimi, _, _ = enim_myydud_album
        print(f'{aastakymne}: {albumite_arv} album(it) ({artist} - {albumi_nimi})')
        
print(kuva(sorteeri("albumid.txt")))
