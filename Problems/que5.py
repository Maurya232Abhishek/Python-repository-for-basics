n=120
i=2
mul=""
s=set({})
while n>1:
    while n%i == 0:
        print(i)
        n /= i
        mul+=str(i)+"x"
        s.add(i)

    i+=1
print(s)
mul=mul[:-1]
print(mul)