n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(n)] for _ in range(n)]

def in_range(x,y) : 
    if x<0 or x>=n or y<0 or y>=n : 
        return False
    return True 

def dfs(x,y) : 

    dxs, dys = [1,0,-1,0],[0,1,0,-1]
    visited[x][y] = 1 
    cnt =1
    for dx,dy in zip(dxs,dys) :
        newx,newy = x+dx, y+dy

        if not in_range(newx,newy) :
            continue 
        
        if visited[newx][newy] ==1 :
            continue
        
        if grid[newx][newy] ==0 : 
            continue 
        
        cnt += dfs(newx,newy)
    
    return cnt



result = []

for i in range(n) :
    for j in range(n) :
        if visited[i][j] ==1 or grid[i][j] ==0 : 
            continue
        
        result.append(dfs(i,j))

result.sort()

print(len(result))
for i in result :
    print(i)
    
