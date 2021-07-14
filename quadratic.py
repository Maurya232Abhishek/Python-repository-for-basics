def QuadraticRegression(px,py):
    sumy = 0
    sumx1= 0
    sumx2= 0
    sumx3 = 0
    sumx4 = 0
    sumxy = 0
    sum2y = 0
    n=len(px)

    for  i in range (n):
        x  = px[i]
        y  = py[i]
        sumx1 += x
        sumy += y
        sumx2 += x*x
        sumx3 += x*x*x
        sumx4 += x*x*x*x
        p = (n * sumxy - sumx1 * sumy) * (n * sumx3 - sumx2 * sumx1) - (n * sumx2 - sumx2 * sumy) * (n * sumx2 - sumx1 * sumx1)
        q = (n * sumx3 - sumx1 * sumx2) * (n * sumx3 - sumx2 * sumx1) - (n * sumx4 - sumx2 * sumx2) * (n * sumx2 - sumx1 * sumx1)
        c = (p/q)
        b = ((n*sumxy - sumx1*sumy) - c*(n*sumx3 - sumx1*sumx2))/(n*sumx2 - sumx1*sumx1)
        a = (sumy - b*sumx1 - c*sumx2)/n
    return a,b,c
x=[0,1,2,3,4]
y=[1,1.8,1.3,2.5,6.3]
print(QuadraticRegression(x,y))



