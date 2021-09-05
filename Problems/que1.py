p=[2,3]
n=500
count = 0
countp = 1

diff=4
i=5
while i<=n : #2  ,3   5,    7,   11,13,17
    if diff==2:
        diff=4
    elif diff==4:
        diff=2

    flag = 1
    for j in p:
        count += 1
        if i%j == 0:
            flag = 0
    if flag == 1:
        p.append(i)
        countp+=1
    i+=diff
print(p)
print(count)
print(len(p))
"""n=8
flag=1 # prime
for i in range(2,int(n**(1/2))+1): #for(int i=2; i<=int(sqrt(2))+1; i++)
    if n%i==0:
        flag=0 #not prim
        break
if flag==1:
    print(n)"""





