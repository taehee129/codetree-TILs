n,k = tuple(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(n)]

start = [tuple(map(int,input().split())) for _ in range(k)]

visited = [[0 for _ in range(n)] for _ in range(n)]

def in_range(x,y) : 
    if x<0 or x>=n or y<0 or y>=n : 
        return False  
    return True 
    
def bfs(x,y) : 
    visited[x][y] = 1 
    q = [(x,y)]

    dxs, dys = [1,0,-1,0], [0,1,0,-1]
    while len(q) > 0 : 
        x,y = q.pop()

        for dx,dy in zip(dxs,dys) : 
            newx,newy = x+dx,y+dy 

            if not in_range(newx,newy) : 
                continue 
            if grid[newx][newy] :
                continue
            if visited[newx][newy] : 
                continue
           
            q.insert(0,(newx,newy))
            visited[newx][newy] = 1 

for x,y in start : 
    bfs(x-1,y-1)

cnt = 0 

for i in range(n) :
    for j in range(n) :
        cnt += visited[i][j]

print(cnt)

        
