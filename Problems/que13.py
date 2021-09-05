s="a aa manas eeeee abhishek shivank punit manjit"
l= s.split()
vowelCount=[]
for i in l:
    count=0
    for j in i:
        j=j.lower()
        if j=="a" or j=="e" or j=="i" or j=="o" or j=="u":
            count+=1
    vowelCount.append(count)
#print(l)
#print(vowelCount)
for i in range(len(vowelCount)-1):
    min=vowelCount[i]
    minpos = i
    for j in range(i+1,len(vowelCount)):
        if vowelCount[j]<min:
            min=vowelCount[j]
            minpos = j
    vowelCount[i],vowelCount[minpos]=vowelCount[minpos],vowelCount[i]
    l[i],l[minpos]=l[minpos],l[i]
print(l)



