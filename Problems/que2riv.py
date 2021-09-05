n=100
count=0
for i in range(1,n+1):
    for j in range(i, n+1):
        k=(i**2+j**2)**(1/2)
        if k<=n and int(k)==k:
            print(i,j,k)
            count+=1
print(count)
