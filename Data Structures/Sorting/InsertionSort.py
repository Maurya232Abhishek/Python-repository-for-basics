a=[11,6,4,5,9,2,7,0,1,-1,-9]
n=len(a)
for i in range(1,n):
    temp=a[i]
    j=i-1
    while j>=0:
        if temp>=a[j]:
            break
        a[j+1]=a[j]
        j-=1
    a[j+1]=temp
print(a)




