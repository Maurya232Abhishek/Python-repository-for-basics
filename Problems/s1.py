s="This is a sentence. Hi I am student. I am costumer"
l=s.split('.')
print(l)
lf=[]
for i in l:
    lf = lf + i.split()
#print(lf)
lengthl=[]
for i in lf:
    lengthl.append(len(i))
print(lf)
print(lengthl)
for j in range(len(lf)):
    min=lengthl[j]
    minpos=j
    for k in range(j,len(lf)):
        if lengthl[k]<min:
            min=lengthl[k]
            minpos=k
    lengthl[j],lengthl[minpos]=lengthl[minpos],lengthl[j]
    lf[j],lf[minpos]=lf[minpos],lf[j]
print(lf)


