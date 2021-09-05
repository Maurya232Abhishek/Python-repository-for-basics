"""a=[5,4,9,8,2,6]
l=0
r=len(a)-1

p=l
for i in range(l+1,r+1):
    if a[l] <=a [i]:
        continue
    p += 1
    a[i],a[p]=a[p],a[i]
a[l],a[p]=a[p],a[l]
print(a)
"""
a=[2,5,8,10]
la=len(a)
b=[3,4,6,7,8,9,11,12,13,14]
l=[]
lb=len(b)
i=0
j=0
while True:
    if i>=la and j>=lb:
        break
    if i>=la:
        l.append(b[j])
        j+=1
        continue
    if j>=lb:
        l.append(a[i])
        i+=1
        continue

    if a[i]<=b[j]:
        l.append(a[i])
        i+=1
    elif a[i]>b[j]:
        l.append(b[j])
        j+=1;
print(l)









