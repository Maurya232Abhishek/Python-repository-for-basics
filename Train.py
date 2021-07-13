train={1:{'Rajhdhani Express':{'stopno':1,{"VNS":0},2:{'LKW':15},3:{'KNP': 45},4:{'ND':60}}},  2:{'Rajhdhani Express':{1:{'ND':0},2:{'KNP':15},3:{'LKW': 45},4:{'VNS':60}}},  3:{'Shivganga':{1:{'VNS':0},2:{'ALD':10},3:{'KNP': 45},4:{'ND':60}}},  4:{'Shivganga':{1:{"ND":0},2:{'KNP':15},3:{'ALD': 50},4:{'VNS':60}}}}

print(train)
while(True):
    print('Type 0 to exit\n 1 to show train \n2 to search train')
    opt =int(input('Enter the option: '))
    if opt==0:
        break
    if opt==1:
        print(train)



    if opt==2:
        x= int(input('Enter the train no. to search :'))

        print(train.get(x))
    if opt==3:
        st="VNS"
        print(st)
        for i in train.keys():

            for j in train.get(i).keys():
                for k in train.get(i).get(j).keys():
                    print(k)
                    if k==st:
                        print("abhi")
                        print(i)

    print('-' * 50)
