import pandas as pd
def div( n):
    result=''
    if n%2==0:
        result= 'Fizz'
    if n%3==0:
        result=result+'Buzz'
    if n%5==0:
        result=result+'Foo'
    if result.__len__()==0:
        return 'Bar'
    else:
        return result

print(div(1))

data= pd.read_csv("D:\Book1.csv")
print(data)

