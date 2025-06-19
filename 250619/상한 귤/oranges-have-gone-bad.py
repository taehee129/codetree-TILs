n,k = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]

rottens = []
times = [[None for _ in range(n)] for _ in range(n)]

for i in range(n) :
    for j in range(n) :
        if grid[i][j] == 2 : 
            rottens.append((i,j))
            times[i][j] = 0 
        if grid[i][j] == 0 :
            times[i][j] = -1 


dxs,dys= [0,1,0,-1],[1,0,-1,0]

def check(x,y) : 
    if x<0 or x>=n or y<0 or y>=n :
        return False 
    return True


while rottens :
    
    x,y = rottens.pop()
    minute = times[x][y] +1
    for dx,dy in zip(dxs,dys) : 
        
        nx,ny = x+dx,y+dy         
        if not check(nx,ny) : 
            continue 
        if times[nx][ny] is not None :
            continue
        
        times[nx][ny] = minute 
        rottens.insert(0,(nx,ny))


for i in range(n) :
    for j in range(n) :
        if grid[i][j] ==1 and times[i][j] is None :
            times[i][j] = -2 
        print(times[i][j], end =' ')
    print()

    