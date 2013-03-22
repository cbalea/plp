'''
Creati un joc in care programul alege un cuvant (din 4 cuvinte posibile definite in program) dupa care spune lungimea lui 
si citeste cate o litera de la tastatura si afiseaza daca litera respectiva face sau nu parte din cuvant. 
Dupa 4 litere jucatorul are 2 incercari sa ghiceasca cuvantul. Daca reuseste a castigat, in caz contrar a pierdut.
'''
import random

cuv1 = "miel"
cuv2 = "caine"
cuv3 = "pisica"
cuv4 = "peste"

index = random.randint(1, 4)
if index==1:
    cuv = cuv1
elif index==2:
    cuv = cuv2
elif index==3:
    cuv=cuv3
else:
    cuv=cuv4

print "Lungimea cuvantului extras este: %d caractere." %len(cuv)

for i in range(1,5):
    litera = raw_input("Indodu o litera: ")
    if litera in cuv:
        print "\t Litera '%s' EXISTA in cuvant." %litera
    else:
        print "\t Litera '%s' NU EXISTA in cuvant." %litera

print "\nIncearca sa ghicesti cuvantul intreg."
castigat=0
for i in range(1,3):
    incercare = raw_input("\t Incercarea %d: " %i)
    if incercare == cuv:
        print "Ai castigat!"
        castigat = 1
        break
if castigat == 0:
    print "Ai pierdut!"