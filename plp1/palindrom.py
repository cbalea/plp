
number=str(raw_input('Scrie numar: '))
nb_of_digits = len(number)

palindrom = True
i = 0
while i <= nb_of_digits/2:
    if number[i] != number[nb_of_digits-i-1]:
        palindrom = False
        break
    i+=1
if palindrom==True:
    print "PALINDROM"
else:
    print "NU e PALINDROM"