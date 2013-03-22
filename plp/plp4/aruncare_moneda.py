'''
Scrieti un program care simuleaza 100 de aruncari a unei monede si afiseaza 
de cate ori a picat pe partea cu cap si de cate ori pe cea cu ban
'''

import random

ban = 0
cap = 0

for i in range(1, 101):
    parte = random.randint(1,2)
    if parte==1:
        ban +=1
    else:
        cap +=1
        
print "BAN a picat de %d ori." %ban
print "CAP a picat de %d ori." %cap