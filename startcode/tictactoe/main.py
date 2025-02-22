# Maak een functie tic_tac_toe(), die ons hele hoofdprogramma bevat
from startcode.tictactoe.mytictactoe import initialiseer_bord, print_bord, controleer_winnaar


def tic_tac_toe():
    bord = initialiseer_bord()
    huidige_speler = "X"
    einde_spel = False
    winnaar = ""
    teller = 0
    while not einde_spel:
        print_bord(bord)
        rij = int(input("Doe een zet. "))
        kolom = int(input("Doe een zet in een kolom"))

        bord = zet(bord, rij, kolom, huidige_speler)

        if(controleer_winnaar(bord) == True):
            print(f"{huidige_speler} Heeft gewonnen!")
            return

        if huidige_speler == "X":
            huidige_speler = "O"
        else:
            huidige_speler = "X"



tic_tac_toe()