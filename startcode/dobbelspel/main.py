import random
# Plaats hierin de main-functie
def is_getal_geraden(gok, geheim_nummer):
    if gok == geheim_nummer:
        print("Correct")
        return True
    else:
        print("Fout")
        return False

def raad_het_getal(bovengrens):
    geheim_nummer = random.randint(1, bovengrens)
    einde_spel = False
    while not einde_spel:
        gok = int(input("Geef een getal"))
        geraden = is_getal_geraden(gok, geheim_nummer)
        if geraden == True:
            einde_spel = True

raad_het_getal(10)