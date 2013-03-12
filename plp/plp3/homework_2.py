'''
Scrieti un program prin care userul introduce valoarea de baza a unei masini. Programul va adauga valoarea altor taxe  
(TVA - procent din valoarea initiala, asigurare, taxa mediu - suma fixa) si va afisa pretul final al masinii.
'''

baza = int(raw_input('Intoru valoarea de baza a masinii: '))

tva = baza*24/100
asigurare = 500
taxa_mediu = 1500

print "\nTAXE:"
print "TVA: %.2f" %tva
print "asigurare: %d" %asigurare
print "taxa mediu: %d" %taxa_mediu
print "\n\nPRET FINAL (cu taxe incluse): %.2f" %(baza + tva + asigurare + taxa_mediu)
