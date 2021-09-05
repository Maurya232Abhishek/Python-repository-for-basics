s="This is a sentence. Hi I am student. I am costumer"
l=s.split('.')
print(l)
lf=[]
for i in l:
    lf = lf + i.split()
print(lf)
countvow=[]
for i in lf:
    count=0
    for j in i:
        j=j.lower()
        if j=="a" or j=="e" or j=="i" or j=="o" or j=="u":
            count += 1
    countvow.append(count)
print(countvow)
for j in range(len(lf)):
    min=countvow[j]
    minpos=j
    for k in range(j,len(lf)):
        if countvow[k]<min:
            min=countvow[k]
            minpos=k
    countvow[j],countvow[minpos]=countvow[minpos],countvow[j]
    lf[j],lf[minpos]=lf[minpos],lf[j]
print(lf)