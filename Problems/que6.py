s="1a3b45Js1hi255"
#print(ord("9"))
l=[]
sum=0
str=""
for i in range(len(s)):
    ascii= ord(s[i])
    if (ascii>=48 and ascii<=57) or ascii==ord("-"):
        str+=s[i]
    else:
        if str=="":
            continue
        l.append(int(str))
        sum+=int(str)
        str=""
    if i==len(s)-1 and ord(s[i])>=48 and ord(s[i])<=57:
        l.append(int(str))
        sum += int(str)

print(sum)
print(l)