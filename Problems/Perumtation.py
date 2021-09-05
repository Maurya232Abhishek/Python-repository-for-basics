count=0
def permute(s,l,n,pos,permuteList):
    if pos>=n:
        #print(l)
        global count

        st=""
        for i in range(n):
            st+=s[l[i]]
        if st not in permuteList:
            count += 1
            print(st)
            permuteList.append(st)
        print()
        return
    for i in range(0,n):
        if i not in l[0:pos]:
            l[pos]=i
            permute(s,l,n,pos+1,permuteList)
s="Manas"
n=len(s)
permuteList=[]
l=[]
for i in range(n):
    l.append(0)
permute(s,l,n,0,permuteList)
print(count)
print(permuteList)