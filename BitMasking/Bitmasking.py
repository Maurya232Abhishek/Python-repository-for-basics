#Bitmasking
# representing subset of natural number till n
# . . . 9 8 7 6 5 4 3 2 1
# . . . 0 0 1 0 0 0 1 1 0
# 0 means that numbers is not there opposite for 1
def display(subset,n):
    for bit_no in range(n):
        if subset & 1<<bit_no:
            print(bit_no + 1,end=" ")
    print()
def remove(set,x): # x is the number you want to remove
    t = set^(1<<x-1)
    return t
def isPresent(set,x): # x is the number
    if set & (1<<(x-1)):
        return 1
    else:
        return 0
def add(set,x):
    if isPresent(set,x):
        print("already Present")
        return set
    else:
        print("added")
        return set | 1<<x-1

subset=15
n=9 # subset is of set of natural till n
#display(subset,n)
subset =remove(subset,3)
subset =  add(subset,3)
print(isPresent(subset,3))
display(subset,n)





