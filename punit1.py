train ={1:'shivganga',2: 'kashi',3: 'rajdhani exp',4: 'mdh exp'}
print (train)
while(True):
    print("0-exit,1-showtrain,2-Addtrain,3-searchtrain")
    opt=int(input("Enter a option"))
    if opt==0:
        break
    if opt==1:
        print(train)
    if opt==2:
        key=int(input('Enter a train no :'))
        value=int(input('Enter a train name :'))
        train[key]=value
    if opt==3:
        trainno=int(input("Enter a search train"))
        x=train.get(trainno)
        print(x)

