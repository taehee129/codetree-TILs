n,k,m = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]

start_points = [tuple(map(int,input().split())) for _ in range(k)]

rocks = []

for i in range(n):
    for j in range(n) :
        if grid[i][j] ==1 :
            rocks.append((i,j))

def check(a,b) :
    if a<0 or a>=n or b<0 or b>=n :
        return False
    return True

def bfs(a,b,grid) : 
    q = []
    q.append((a,b))
    cnt =1
    grid[a][b] = 2
    dxs,dys = [0,1,0,-1],[1,0,-1,0]
    while q : 
        x,y =q.pop()
        
        for dx,dy in zip(dxs,dys) :
            nx,ny = x+dx,y+dy 

            if not check(nx,ny) :
                continue 
            if grid[nx][ny] == 1 :
                continue
            if grid[nx][ny] == 2 :
                continue
            q.insert(0,(nx,ny))
            grid[nx][ny] = 2 
            cnt +=1
    
    return grid

def print_grid(grid) : 
    for i in range(n) :
        for j in range(n) :
            print(grid[i][j],end =' ')
        print()

lst =[]
def simul() : 
    cnt = 0
    new_grid = [[grid[i][j] for j in range(n)] for i in range(n)]
    for i in lst : 
        x,y = rocks[i]
        new_grid[x][y] = 0 
    
    for x,y in start_points : 
        x -=1 
        y -=1
        new_grid = bfs(x,y,new_grid)
    
    #print_grid(new_grid)

    for i in range(n) :
        for j in range(n) :
            if new_grid[i][j] == 2 :
                cnt +=1
    #print(cnt)
    return cnt

ret = 0
def permu(s,e,cnt) : 
    global ret
    if cnt == m : 
        ret = max(simul(),ret)
       
    for i in range(s,e):
        lst.append(i)
        permu(i+1,e,cnt+1)
        lst.pop()
    
    
permu(0,len(rocks),0)
print(ret)