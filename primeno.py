
s=10
e=100
for i in range(s,e):
    flag=1
    for j in range(2,int(i**(1/2))+1):
        if i%j==0:
            flag=0
    if flag==1:
        print(i,end=",")
