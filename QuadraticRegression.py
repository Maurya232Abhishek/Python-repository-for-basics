# y= a+bx+cx^2
def QuadraticRegression(px, py):
    sumy = 0
    sumx = 0
    sumx2 = 0
    sumx3 = 0
    sumx4 = 0
    sumxy = 0
    sumx2y =0
    n=len(px)

    for i in range(n):
        x = px[i]
        y = py[i]
        sumx += x
        sumy += y
        sumx2 += x*x
        sumx3 += x*x*x
        sumx4 += x*x*x*x
        sumxy += x*y
        sumx2y += x*x*y
    p = (n * sumxy - sumx * sumy) * (n * sumx3 - sumx2 * sumx) - (n * sumx2y - sumx2 * sumy) * (n * sumx2 - sumx * sumx)
    q = (n * sumx3 - sumx * sumx2) * (n * sumx3 - sumx2 * sumx)-(n * sumx4 - sumx2 * sumx2)* (n * sumx2 - sumx * sumx)

    c = (p/q)
    b = ((n*sumxy - sumx*sumy) - c*(n*sumx3 - sumx*sumx2))/(n*sumx2 - sumx*sumx)
    a = (sumy - b*sumx - c*sumx2)/n

    return a,b,c
x = [0,1,2,3,4]
y = [1,1.8,1.3,2.5,6.3]
print(QuadraticRegression(x,y))