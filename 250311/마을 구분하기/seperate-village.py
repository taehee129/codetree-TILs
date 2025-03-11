n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(n)] for _ in range(n)]

def in_range(x,y) : 
    if x<0 or x>=n or y<0 or y>=n : 
        return False
    return True 

def dfs(x,y) : 

    if not in_range(x,y) :
        return 0
    
    if visited[x][y] ==1 :
        return 0
    
    if grid[x][y] ==0 : 
        return 0 
    

    dxs, dys = [1,0,-1,0],[0,1,0,-1]
    visited[x][y] = 1 
    cnt =1

    for dx,dy in zip(dxs,dys) :
        newx,newy = x+dx, y+dy        
        cnt += dfs(newx,newy)
    
    return cnt



result = []

for i in range(n) :
    for j in range(n) :
                
        val = dfs(i,j)
        if val !=0 :
            result.append(val)

result.sort()

print(len(result))
for i in result :
    print(i)
    
