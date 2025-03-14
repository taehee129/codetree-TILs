n,m = tuple(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(n)]


def in_range(x,y) : 
    if x<0 or x>=n or y<0 or y>=m : 
        return False
    return True
def melt(x,y) :
    dxs,dys= [1,0,-1,0], [0,1,0,-1]
    
    for dx,dy in zip(dxs,dys) : 
        nx,ny = x+dx,y+dy 

        if not in_range(nx,ny) : 
            continue 
        if grid[nx][ny] == 1 :
            new_grid[nx][ny] = 0
def bfs(start_x,start_y) : 
    
    q = [(start_x,start_y)]
    visited[start_x][start_y] = 1 
    dxs,dys= [1,0,-1,0], [0,1,0,-1] 

    while len(q) >0 : 
        x,y = q.pop()

        for dx,dy in zip(dxs,dys) : 
            nx,ny = x+dx,y+dy 
            
            if not in_range(nx,ny) : 
                continue
            if visited[nx][ny] : 
                continue
            if grid[nx][ny] == 1 :
                continue
            
            q.insert(0,(nx,ny))
            visited[nx][ny] = 1 
            melt(nx,ny)


def check(x,y) : 
    dxs,dys= [1,0,-1,0], [0,1,0,-1]
    
    for dx,dy in zip(dxs,dys) : 
        nx,ny = x+dx,y+dy 

        if not in_range(nx,ny) : 
            continue 
        
        if grid[nx][ny] == 0 :
            return True 
    
    return False


def count_ice(grid) : 
    cnt=0
    for i in range(n) :
        for j in range(m) : 
            cnt+= grid[i][j]
    return cnt 
time =0
while True : 
    time +=1
    new_grid = [grid[i][:] for i in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    bfs(0,0)

    if count_ice(new_grid) == 0 : 
        
        print(time,count_ice(grid))
        break
    
    grid = new_grid

