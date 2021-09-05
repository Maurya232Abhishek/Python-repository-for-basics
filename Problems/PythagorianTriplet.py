n=100
count=0
for i in range(1,n+1):
    for j in range(i+1,n+1):
        t=(i**2+j**2)**(1/2)
        if t==int(t) and t<=100:
            print(t)
            #print(i,j,t)
            count+=1
print(count)
"""n=100
count=0
for i in range(1,n+1):
    for j in range(i,n+1):
        for k in range(j+1,n+1):
            if i**2+j**2==k**2:
                count+=1
                print(i,j,k)
print(count)"""
