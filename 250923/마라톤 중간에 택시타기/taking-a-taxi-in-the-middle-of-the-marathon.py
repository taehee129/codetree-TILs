n = int(input())

points = [tuple(map(int,input().split())) for _ in range(n)]

L= [0]*n
R= [0]*n

for i in range(1,n) :
    x1,y1 = points[i-1]
    x2,y2 = points[i]
    L[i] = L[i-1] + abs(x1-x2) + abs(y1-y2)

for i in range(n-2,-1,-1) :
    x1,y1 = points[i+1]
    x2,y2 = points[i]

    R[i] = R[i+1] + abs(x1-x2) + abs(y1-y2)


import sys
MIN_SIZE = sys.maxsize 

ans = MIN_SIZE 

for i in range(1,n-1) :
    x1, y1 = points[i-1]
    x2,y2 = points[i+1]

    distance =  abs(x1-x2) + abs(y1-y2) + L[i-1] + R[i+1]

    ans = min(ans,distance) 



print(ans)
