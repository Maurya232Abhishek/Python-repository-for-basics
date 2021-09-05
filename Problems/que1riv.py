n=500
primeno=[2,3]
i=5
flag=0
diff=2
while i<=500:
    print(i)
    flag_p=1
    for j in primeno:
        if i%j== 0:
            flag_p = 0
            break
    if flag_p==1:
        primeno.append(i)
    i += diff
    if flag == 0:
        diff=4
        flag=1
        continue
    if flag == 1:
        diff=2
        flag=0
print(primeno)
print(len(primeno))





