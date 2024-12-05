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

def left(x,y,d) :
    d = (d-1)%4
    x,y =x+dx[d],y+dy[d]
    return x,y,d


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


while True : 

    if not valid(x,y) :
        break
    if cnt !=0 and x==orginX and y == originY : 
        cnt =-1
        break 
    
    forwardx,forwardy,forwardd= forward(x,y,d)
    cnt+=1
    if valid(forwardx,forwardy) and grid[forwardx][forwardy] == brick : # 앞에 벽돌 이 있다면 
        x,y,d = left(x,y,d)
        
        continue

    rightx,righty,rightd = right(forwardx,forwardy,forwardd)

    if valid(rightx,righty) and grid[rightx][righty] != brick : #
        x,y,d= rightx,righty,rightd
        cnt+=1
    else :
        x,y,d = forwardx,forwardy,forwardd


print(cnt)
