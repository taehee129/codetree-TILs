# 앞에 벽이 있을 때
# 반 시계 방향으로 간다.  
#
# 앞에 벽이 없고 
# 가는 방향에 오른쪽 벽이 있는 경우 
#  1. 그냥  앞으로 간다.
# 가는 방향에 오른쪽에 벽이 없는 경우 
#  1. 탈출  
#  2. 시계 방향으로 90 

dx,dy =[0,1,0,-1],[1,0,-1,0]

n = int(input())

def valid(x,y) : 
    if (x>=n or x<0) or (y>=n or y<0) :
        return False
    return True 


def forward(x,y,d) :

    x,y = x+dx[d],y+dy[d]
    return x,y,d


def right(x,y,d) :
    d = (d+1)%4
    x,y =x+dx[d],y+dy[d]
    return x,y,d

def left(d) :
    d = (d-1)%4

    return d

x,y = tuple(map(int,input().split()))
grid = [
    input()
    for _ in range(n)
]

x-=1
y-=1
orginX,originY = x,y
brick = "#"
d = 0
cnt=0

leftCnt=0
sameCnt=0

while True : 
    
    if leftCnt == 4 :
        cnt =-1
        break
    if not valid(x,y) :
        break
    if cnt !=0 and x==orginX and y == originY : 
        sameCnt +=1
        if sameCnt ==2 :
            cnt=-1
            break 
    forwardx,forwardy,forwardd= forward(x,y,d)

    if valid(forwardx,forwardy) and grid[forwardx][forwardy] == brick : # 앞에 벽돌 이 있다면 
        
        d = left(d)
        leftCnt+=1
        continue
    leftCnt=0
    x,y,d = forward(x,y,d)
    print(x,y,d)
    cnt+=1
    rightx ,righty, rightd = right(x,y,d)
    if valid(rightx,righty) and grid[rightx][righty] != brick : #
        x,y,d = right(x,y,d)
        print(x,y,d)
        cnt+=1
        continue


   
    

print(cnt)
