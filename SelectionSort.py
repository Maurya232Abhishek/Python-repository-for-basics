l=[9,7,4,8,43,3,5,1,10,-1]
print(l)

for i in range(0, len(l)-1):
   min = l[i]
   minpos = -1

   for j in range(i,len(l)):
       if l[j]<=min:    
           min=l[j]
           minpos=j


   print(minpos)
   l[i],l[minpos]=l[minpos],l[i]


print(l)