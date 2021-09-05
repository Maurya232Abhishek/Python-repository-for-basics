count=0
def permute(s,l,pos,n):
    if pos>=n:
        global count
        count+=1
        print(l)
        for k in l:
            print(s[k],end="")
        print()
        return
    for i in range(n):
        if i not in l[:pos]:
            l[pos] = i
            permute(s,l,pos+1,n)



s="shivank"
n=len(s)
l=[]
for i in range(n):
    l.append(0)

permute(s,l,0,n)
print(count)