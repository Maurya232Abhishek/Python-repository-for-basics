"""n=5
i=2
s=""
while n>1:
    while n % i ==0:
        print(i)
        s+=str(i)+"x"
        n /= i

        if n == 1:
            break
    i+=1
s=s[:-1]
x=[]

print(s)
x={1,2,3,4,5,3,2}
x.add(9)
print(x)
s="abhishe"

l = input().split()
for i in l:

    i= int(i)

print(l)"""
no,l,base=31,2,30

#base=30
#l=3
"""dict={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
minsum=0
minbase=0

for i in range(l,base+1):
    convertedNum = []
    n=no
    sum = 0
    while(n>0):
        convertedNum= [n % i] +convertedNum
        sum += n % i
        n=n//i
        if i != l and sum>=minsum:
            break
    if i == l:
        minsum=sum
        minbase = i
    elif sum<minsum:
        minsum = sum
        minbase = i
        print(i,convertedNum," = ",sum)
print(minbase,minsum)"""
"""words=["a","b","c","d","e","f","g"]
count = [11,6,4,2,1,-1,0,-2,10,-3,-5]
for i in range(1, len(count)):
    print(i,count)
    tempc = count[i]
    #tempw = words[i]
    j = i - 1
    while j >= 0:
        if count[j] > tempc:
            count[j + 1] = count[j]
            #words[j + 1] = words[j]
        else:
            break
        j -= 1
    j += 1
    print(i,j,tempc)
    count[j] = tempc
    #words[j] = tempw
print(count)
print(words)
st=" abhis "
print("a",end="")
print(st.strip(),end="")
print(st)"""
l=["abhi","ram","shame","rem"]
l = [2,3,8,5,4,3]
print(set(l))


