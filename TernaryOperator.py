a=1
b=2
c=3
max = a if a>=b else b
print(max)
max = (a if a>=c else c) if a>=b else (b if b>=c else c)
print(max)