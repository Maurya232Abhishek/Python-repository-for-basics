s="112353211"
#print(len(s)//2)
flag=1
for i in range(len(s)//2):
    j= len(s)-1-i
    if s[i] != s[j]:
        flag=0
        break
if flag==1:
    print("Panlindrome")
else:
    print("NOT palindrome")