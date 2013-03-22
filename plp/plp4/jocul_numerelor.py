'''
Scrieti un program care simuleaza "jocul numerelor" dar cu rolurile inversate decat cel facut la curs. 
Jucatorul isi alege un numar aleator intre 1 si 100 iar calculatorul incearca sa il ghiceasca. 
Dupa fiecare incercare jucatorul trebuie sa comunice programului daca incercarea a fost corecta, 
mai mica sau mai mare decat numarul ales.
'''

start=1
end=100
gasit = False

while not gasit:
    incercare = (start + end)/2
    print "Incerc cu %d" %incercare
    mesaj = int(raw_input("Daca numarul incercat este \n'mai mic' apasa -1 \n'mai mare' apasa 1 \n'ghicit' apasa 0 \n"))
    if mesaj == -1:
        start = incercare - 1
    elif mesaj ==1:
        end = incercare + 1
    else:
        print "Ai ghicit!"
        gasit = True
    