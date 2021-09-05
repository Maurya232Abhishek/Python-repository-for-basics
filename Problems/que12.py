#Armstrong Number
n="407"
sum=0
for i in range(len(n)):
    sum += int(n[i])**3
if int(n)==sum:
    print("Given Number is Armstrong Number")
else:
    print("Not a Armstrong Number")
