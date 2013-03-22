'''
Scrieti un program care simuleaza "jocul numerelor" dar cu rolurile inversate decat cel facut la curs. 
Jucatorul isi alege un numar aleator intre 1 si 100 iar calculatorul incearca sa il ghiceasca. 
Dupa fiecare incercare jucatorul trebuie sa comunice programului daca incercarea a fost corecta, 
mai mica sau mai mare decat numarul ales.
'''
import random

mesaj = None

while mesaj != 0:
    incercare = random.randint(1, 100)
    print "Incerc cu %d" %incercare
    mesaj = int(raw_input("Daca numarul incercat este \n'mai mic' apasa -1 \n'mai mare' apasa 1 \n'ghicit' apasa 0 \n"))
    if mesaj == -1:
        incercare = random.randint(incercare, 100)
    elif mesaj ==1:
        incercare = random.randint(1, incercare)
    else:
        print "Am ghicit!"
    