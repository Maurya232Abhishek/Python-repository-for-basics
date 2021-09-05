a=[-1,1,9,2,8,3,7,4,5,6,0,12]
n= len(a)
for i in range(n-1):
    for j in range(n-i-1):
        if a[j+1]<a[j]:
            a[j+1],a[j]=a[j],a[j+1]
print(a)