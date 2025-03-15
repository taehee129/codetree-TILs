n,h,m = tuple(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(n)]



def in_range(x,y) :
    if x<0 or x>=n or y<0 or y>=n :
        return False 
    return True 

def bfs(x,y) : 
    
    step[x][y] = 1 
    q = [(x,y)]
    dxs,dys= [1,0,-1,0],[0,1,0,-1]
    while len(q) > 0 :
        x,y = q.pop()

        for dx,dy in zip(dxs,dys) : 
            nx,ny = x+dx,y+dy 
           
            if not in_range(nx,ny) :
                continue 
            
            if grid[nx][ny] ==1 :
                continue
            
            if step[nx][ny] !=0 : 
                continue 
            
            q.insert(0,(nx,ny))
            step[nx][ny] = step[x][y] +1 
            if grid[nx][ny] == 3 :
                return step[nx][ny]-1 
    
    return -1 

aws = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n) : 
    for j in range(n) : 
        if grid[i][j] != 2 : 
            continue
        step = [[0 for _ in range(n)] for _ in range(n)]
        aws[i][j] = bfs(i,j)
        

for i in aws :
    print(' '.join(list(map(str,i))))


    
