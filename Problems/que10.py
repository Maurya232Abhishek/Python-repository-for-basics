#Happy Numbers
n="188"
t=n
sum=0
l=[]
flag=1
while True:
    sum=0
    for i in range(len(t)):
        sum+=int(t[i])**2
    if sum==1:
        flag=1
        break
    if sum in l:
        flag=0
        break
    l.append(sum)
    t=str(sum)
if flag==0:
    print("not a Happy Number")
else:
    print("Is a Happy Number")

