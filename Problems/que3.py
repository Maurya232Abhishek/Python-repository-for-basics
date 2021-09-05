s="211101112"
l=len(s)
#print(l)
n=len(s)//2
if l%2==0:
    n=len(s)//2+1
count=0

for i in range(1 , n+1):
    i1=i-1
    j=-i
    if s[i1]==s[j]:
        print(s[i1])
        print(s[j])
        count+=1
if count==n:
    print("it is palindrome")
else:
    print("not a palindrome")