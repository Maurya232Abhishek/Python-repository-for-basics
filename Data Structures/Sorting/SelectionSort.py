l=[2,4,5,6,7,8]
n=len(l)
for i in range(n):
    min=l[i]
    minpos=i
    for j in range(i+1,n):
        if l[j]<min:
            min=l[j]
            minpos=j
        l[i],l[minpos]=l[minpos],l[i]

print(l)