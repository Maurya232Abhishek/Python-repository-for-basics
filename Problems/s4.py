s="and nda this isth ram mra the eth same emas then"
l=s.split(".")
lf=[]
for i in l:
    lf += i.split()
mark=[]
for i in range(len(lf)):
    mark.append(0)
print(lf)
for i in range(len(lf)):
    if mark[i]==1:
        continue
    s1=lf[i]
    ls1=list(s1)
    print(s1,end="=")
    mark[i]=1
    for j in range(i+1,len(lf)):
        s2=lf[j]
        ls2=list(s2)
        if len(s1)==len(s2):
            for k in s1:
                if k not in s2:
                    break
                ls2.remove(k)
        if len(ls2) == 0:
            print(s2,end=",")
            mark[j]=1
    print("")


