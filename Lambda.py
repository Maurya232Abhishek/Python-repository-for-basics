import functools as ft
def mycompare(a,b):
    return a-b
class Book:
    def __init__(self,bookname,subject,price):
        self.bookname = bookname
        self.subject = subject
        self.price = price
print("Lambda")
f = lambda : print("Hello lambda")
f()
f = lambda name : print("Hello " + name)
f("Abhishek")
f = lambda a,b : print(a+b)
f(1,6)
f = lambda a,b : print(a) if a>b else print(b)
f(7,9)
f = lambda book : print("bookname= "+ book.bookname)
f(Book(" Adv Python","Python","150"))
f(Book("Java","Java","151"))
l = ["Apple","Ball","Cat"]
l.sort(key =lambda x:x[0]) # sort according to the 0th index value
print(l)
l=[1,2,9,4,5]
l.sort(key=ft.cmp_to_key(mycompare)) #
print(l)