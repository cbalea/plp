sir=[1, 4, 6, 2, 0, 3, 5]
leng = len(sir)

print leng

for i in xrange(leng):
    for j in xrange (i, leng):
        if sir[i] > sir[j]:
            aux=sir[j]
            sir[j]=sir[i]
            sir[i]=aux

print sir