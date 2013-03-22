'''
Creati un program care citeste un mesaj de la tastatura dupa care il afiseaza in ordine inversa cate un caracter pe linie.
'''

mesaj = raw_input("Scrie mesajul: ")

i=0
for leter in mesaj:
    i+=1
    print mesaj[-i]
