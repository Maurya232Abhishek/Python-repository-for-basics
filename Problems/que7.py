s="(as(2(as)asdf))"
openpos=[] # contains position of opening brackets
closepos=[] #contains position of closing brackets
count=0
flag = 1
for i in range(len(s)):
    if s[i]== "(":
        count+=1
        openpos.append(i)
    elif s[i] == ")":
        count -= 1
        closepos.append(i)
    if count<0:
        flag = 0
        break
if count != 0:
    flag=0
print(flag)
print(openpos,closepos)

#############################@@@@@@@
d=[]
if flag == 1 :
    for i in range(len(openpos)):
        j=len(openpos)-1-i
        d.append(s[openpos[j]+1:closepos[i]])

print(d)



