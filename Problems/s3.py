s1="This is a sentence. Hi This is Abhishek"
s2="This is a sentence. Hi I am student. I am costumer"
l1=s1.split(".")
l2=s2.split(".")
lf1=[]
lf2=[]
for i in l1:
    lf1 += i.split()
for i in l2:
    lf2 += i.split()
print(lf1)
print(lf2)
set1=set(lf1)
set2=set(lf2)
print(set1.intersection(set2))
