n,m = tuple(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(n)]

visited  = [[0 for _ in range(m)] for _ in range(n)] 

def in_range(x,y) : 
    if x<0 or x>=n or y<0 or y>=m : 
        return False 
    return True

def dfs(x,y) : 
    if x==n-1 and y == m-1 : 
        return True              
    dxs,dys = [1,0], [0,1] 

    for dx,dy in zip(dxs,dys) : 
        newx,newy = x+dx , y+dy 
        if not in_range(newx,newy) :
            continue
        if grid[newx][newy] == 0 :
            continue 
        if visited[newx][newy] ==1 : 
            continue
        
        visited[newx][newy] = 1  
        return dfs(newx,newy)
    

visited[0][0] =1 

if dfs(0,0) : 
    print(1)
else :
    print(0)