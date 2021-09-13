inf=1000
dict={0:"A",1:"B",2:"C",3:"D",4:"E"}
mark=[0,0,0,0,0] # to mark that the number is seleceted as min and cannot be selected as min further process
# we can even store position selected as min value for same above reasons
path=["A","A->B","A->C","A->D","A->F"]
g=[
    [-1 , 10 , 5 ,inf,inf],
    [inf,-1 , 2 , 1 , inf],
    [inf, 3 , -1 , 9 , 2 ],
    [inf,inf,inf, -1 , 4 ],
    [ 7 ,inf,inf, 6 , -1 ]
]

for k in range(4):

    print(g[0])
    #print(mark)
    min = inf
    minpos = -1
    for i in range(5):

        if g[0][i] != -1:
            #print(-1,i)

            if mark[i] != 1 and min > g[0][i]:

                #print("min pos",i)
                min = g[0][i]
                minpos = i
    mark[minpos] = 1
    #print("ming",minpos,min)
    if minpos == -1:
        continue
    for j in range(5):
        if minpos == j:
            continue
        if g[minpos][j] == -1 or g[minpos][j] == inf:
            continue
        sum = min + g[minpos][j]
        #print(g[0][j],sum)
        if g[0][j] > sum:
            g[0][j] = sum
            path[j]="A->"+dict[minpos]+"->"+dict[j]
print(g)
print(path)



