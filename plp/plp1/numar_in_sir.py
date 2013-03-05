
number=int(raw_input('Scrie numar: '))
sir=map(int, raw_input('Scrie sir de numere crescator: ').split())

nb_of_items = len(str(sir))

este = False
i=0
while sir[i]<=number:
    if sir[i] == number:
        este = True
        break
    i+=1
if este == True:
    print "Numar E in sir"
else:
    print "Numar NU E in sir"

