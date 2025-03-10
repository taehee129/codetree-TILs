n,m = tuple(map(int,input().split()))
result = 0
grid = [list(map(int,input().split())) for _ in range(n)]

visited  = [[0 for _ in range(m)] for _ in range(n)] 

def in_range(x,y) : 
    if x<0 or x>=n or y<0 or y>=m : 
        return False 
    return True

def dfs(x,y) :
    global result 
    if x==n-1 and y == m-1 : 
        result = 1      
    dxs,dys = [1,0], [0,1] 
    visited[x][y] = 1
    for dx,dy in zip(dxs,dys) : 
        newx,newy = x+dx , y+dy 
        if not in_range(newx,newy) :
            continue
        if grid[newx][newy] == 0 :#if there is snake
            continue 
        if visited[newx][newy] ==1 : # already visited 
            continue
        
        dfs(newx,newy)
    

dfs(0,0)

print(result)