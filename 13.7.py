d={}
top=-1
while (True):
    x=input("Enter the word:")
    x=x.strip()
    if x=='0':
        break
    if x not in d.keys():
        d[x]=1
    else:
        d[x]=d[x]+1
    # n=input("Do you want to exit?(type y for yes and n for no)")
    #if(n=='y' or n=='y'):
    # break
s=d.values();
l=list(s)
#s.pop(2)
#print(s)
m1=max(l)
l.remove(m1)
#print(m1)
m2=max(1)
l.remove(m2)
#print(m2)
m3=max(l)
l.remove(m3)
#print(m3)
m4=max(l)
l.remove(m4)
#print(m4)
m5=max(l)
#print(m1,m2,m3,m4,m5)

for a in d.keys():
    if m1==d[a]:
        print(a)
        w1=a
        break
for a in d.keys():
    if m2==d[a] and a!=w1:
        print(a)
        w2=a
        break
for a in d.keys():
    if m3==d[a] and a!=w2:
        print(a)
        w3=a
        break
for a in d.keys():
    if m4==d[a] and a!=w3:
        print(a)
        w4=a
        break
for a in d.keys():
    if m5==d[a] and a!=w4:
        print(a)
        w5=a
        break







