#Perfect  Number
n=6
t=n
properFactor=set({1})
#print(properFactor)
i=2
sum=1
while t>1:
    #print(t)
    while t%i==0 :
        t=t/i
        properFactor.add(i)
    if i in properFactor:
        sum+=i
    i+=1
if n==sum:
    print("Given number is Perfect Number")


