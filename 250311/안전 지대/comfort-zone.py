n,m = tuple(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(n)]


def in_range(x,y) : 
    if x<0 or x>=n or y<0 or y>=m :
        return False
    return True  


def dfs(x,y) : 
    global k
    dxs,dys = [0,1,0,-1], [1,0,-1,0] 
    visited[x][y] = 1 
    for dx,dy in zip(dxs,dys) : 
        newx,newy = x+dx,y+dy 

        if not in_range(newx,newy):
            continue 
        if visited[newx][newy] : 
            continue
        if grid[newx][newy] <= k :
            continue

        dfs(newx,newy)


def search(k) : 
    cnt =0
    for i in range(n) :
        for j in range(m) : 
            if visited[i][j] == 1 or grid[i][j] <= k :
                continue
            dfs(i,j)
            cnt+=1 
    
    return cnt
            

max_k =0 

for i in range(n) : 
    for j in range(m) : 
        max_k = max(max_k, grid[i][j])

max_cnt = 0
result = 0
for k in range(max_k,0,-1) :
    visited = [[0 for _ in range(m)] for _ in range(n)]

    val = search(k)
    if max_cnt < val :
        max_cnt = val 
        result = k 

print(result, max_cnt)

            
            