'''
Scrieti un program care simuleaza 100 de aruncari a unei monede si afiseaza 
de cate ori a picat pe partea cu cap si de cate ori pe cea cu ban
'''

import random

for i in range(1, 101):
    parte = random.randint(1,2)
    mesaj = "aruncare %s - " %i
    if parte==1:
        mesaj += "BAN"
    else:
        mesaj += "CAP"
    print mesaj
        

