s="This is a sentence. I am Abhishek. Hi how are you."
l=s.split(".")
lf=[]
for i in l:
    lf += i.split()
print(lf)
c=[]
for i in lf:
    c += [char.lower() for char in i]
c.sort()
c=set(c)

print(c)
