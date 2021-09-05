n=5
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

print(l)