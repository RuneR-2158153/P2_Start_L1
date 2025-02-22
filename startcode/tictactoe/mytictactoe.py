def initialiseer_bord():
    # bord = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    bord = []
    for rij in range(3):
        rij_inhoud = []
        for kolom in range(3):
            rij_inhoud.append(' ')
        bord.append(rij_inhoud)
    return bord


def zet(bord, rij, kolom, huidige_speler):
    bord[rij][kolom] = huidige_speler
    return bord


def print_bord(bord):
    print("")
    for rij in bord:
        print('|'.join(rij))
        print("----------")

def controleer_winnaar(bord):
    if controleer_horizontaal(bord) or controleer_verticaal(bord):
        return True
    else:
        return False
def controleer_horizontaal(bord):
    for rij in bord:
        if rij[0] == rij[1] == rij[2] != ' ':
            return True
    return False

def controleer_verticaal(bord):
    for kolom in range(3):
        if bord[0][kolom] == bord[1][kolom] == bord[2][kolom] != ' ':
            return True
    return False


def controleer_diagonaal(bord):
    pass