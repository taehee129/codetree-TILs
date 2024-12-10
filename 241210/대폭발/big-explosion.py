n,m,r,c = tuple(map(int,input().split()))
r -=1
c -=1
grid = [
    [0 for _ in range(n)] for _ in range(n) 
]

def valid(x,y) :
    if x<0 or x>=n or y<0 or y>=n :
        return False
    return True


grid[r][c] = 1 

dx,dy=[1,-1,0,0] , [0,0,1,-1]

for t in range(1,m+1) :
    newGrid = [
        lst[:] for lst in grid
    ]
    for i in range(n) :
        for j in range(n) :
            for k in range(4) :
                x,y = i+(dx[k]*2**(t-1)),j+(dy[k]*2**(t-1))
                if not valid(x,y) :
                    continue
                               
                if grid[x][y] == 1 :
                    
                    newGrid[i][j] = 1 
    
    grid = [
        lst[:] for lst in newGrid
    ]

cnt = 0                
for i in range(n) :
    for j in range(n) :
        if grid[i][j] ==1 :
            cnt +=1

print(cnt)
