def CorrelationCoefficient(px,py):
    n=len(px)
    sumx = 0
    sumy = 0
    sumXY = 0 # submission X=x-x1 Y=y-y1

    sumX2 = 0
    sumY2 = 0
    for i in range(n):
        x = px[i]
        y = py[i]
        sumx += x
        sumy += y
    x1 = sumx/n  #mean of x
    y1 = sumy/n #mean of y
    for i in range(n):
        X = px[i] - x1
        Y = py[i] - y1
        sumXY += X*Y

        sumX2 += X*X
        sumY2 += Y*Y
    return sumXY/(sumX2*sumY2)**(1/2)
x = [0,1,2,3,4]
y = [4-1,6-1,8-1,10-1,12-1]
print(CorrelationCoefficient(x,y))


