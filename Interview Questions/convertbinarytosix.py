ip= [0,0,1,1]
ipbase=2
opbase=6
op=[]
decimal=0
m=1
for i in ip:
    decimal=decimal +i * m
    m=m*ipbase
print(decimal)
while decimal>0:
    rem = decimal % opbase
    decimal=decimal//opbase
    op =  op + [rem]
print(op)

