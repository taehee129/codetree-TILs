n,k = tuple(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(n)]

x,y = tuple(map(int,input().split()))
x,y = x-1,y-1

def in_range(x,y) : 
    if x<0 or x>=n or y<0 or y>=n :
        return False
    return True
def bfs(x,y) : 
    q = [(x,y)]
    sx,sy = x,y
    dxs ,dys = [1,0,-1,0],[0,1,0,-1]
    maxVal = 0 
    rx,ry = (x,y)

    while len(q) >0 : 

        x,y = q.pop()

        for dx,dy in zip(dxs,dys) : 
            nx,ny = x+dx,y+dy 
            
            if not in_range(nx,ny) :
                continue 
            if visited[nx][ny] == 1 :
                continue 
            if grid[nx][ny] >= grid[sx][sy] :
                continue
            
            q.insert(0,(nx,ny))
            visited[nx][ny] = 1 
            
            if (maxVal, -rx,-ry) < (grid[nx][ny],-nx,-ny):
                (maxVal, rx,ry) =  (grid[nx][ny],nx,ny)
             
    return rx,ry 

for _ in range(k) :
    visited= [[0 for _ in range(n)] for _ in range(n)] 
    x,y = bfs(x,y)
print(x+1,y+1)            

