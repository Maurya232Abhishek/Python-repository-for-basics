n=60
t=n
primeFactor=set()
i=2
while t>1:
    while t%i == 0:
        t = t/i
        primeFactor.add(i)
    i += 1
print(primeFactor)