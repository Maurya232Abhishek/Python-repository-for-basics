n=1000
base=16
dict={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
convertedNum=""
while(n>0):
    if n%base>=10:
        convertedNum=dict[(n % base)] + convertedNum
    else:
        convertedNum= str(n % base) +convertedNum
    n=n//base
print(convertedNum)

