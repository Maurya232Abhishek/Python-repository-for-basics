
s="24234712391238947"
print(len(s))
if len(s)%3!=0:
    if len(s)%3==1:
        s="00"+s
    if len(s)%3==2:
        s="0"+s

#i = int(s)
print(len(s))
a=[0,0,0]
t=1
for i in range(0,len(s),3):
    print(i)

    j=len(s)-1-i
    print(j)
    if t == 1:
        a[0]=a[0]+int(s[j])
        a[1]=a[1]+int(s[j-1])
        a[2]=a[2]+int(s[j-2])
        t=0
    elif t==0:
        a[0] -= int(s[j])
        a[1] -= int(s[j-1])
        a[2] -= int(s[j-2])
        t=1

rem = a[0]*1+a[1]*3+a[2]*2
print(rem%7)
