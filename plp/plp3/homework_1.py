'''
Scrieti un program prin care userul introduce valoarea notei de la restaurant. 
Programul va afisa valoarea TVA-ului si valoarea bacsisului (15%).
'''

nota = float(raw_input('Intoru valoarea notei de plata: '))



print "TVA: %.2f ron" % (nota - 100*nota/(100+24))
print "Bacsis: %.2f ron" %(nota*15/100)