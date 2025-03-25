n,k = tuple(map(int,input().split()))

origin_grid = [list(map(int,input().split())) for _ in range(n)]

start_x,start_y = map(int,input().split())

end_x, end_y = map(int,input().split())


wall_list = [ (i,j) for i in range(n) for j in range(n) if origin_grid[i][j] == 1 ]


combinations =[]
clist = []
end = len(wall_list)
def combinate(idx):

    if len(clist)== k : 
        combinations.append(clist[:])
    
    for i in range(idx, end) : 
        clist.append(i)
        combinate(i+1)
        clist.pop()

combinate(0)


def in_range(x,y) : 
    if x<0 or x>=n or y<0 or y>=n :
        return False
    return True


def bfs(x,y,grid) : 
    elapsed_time = [[0 for _ in range(n)] for _ in range(n)]
    visited=[[0 for _ in range(n)] for _ in range(n)]

    q = [(x,y)]
    visited[x][y] = 1
    dxs,dys = [1,0,-1,0],[0,1,0,-1] 

    while len(q) >=1 : 

        x,y = q.pop()

        for dx,dy in zip(dxs,dys) : 
            nx,ny = x+dx,y+dy 

            if not in_range(nx,ny) :
                continue 
            if visited[nx][ny] :
                continue
            if grid[nx][ny] == 1 :
                continue 
            
            if (nx,ny) == (end_x-1,end_y-1) : 
                return elapsed_time[x][y] +1

            q.insert(0,(nx,ny))
            visited[nx][ny] = True
            elapsed_time[nx][ny] = elapsed_time[x][y] +1

    return False

import sys 

MAX_VAL = sys.maxsize
min_elapsed_time = MAX_VAL

for com in combinations : 
    grid = [origin_grid[i][:] for i in range(n)]
    for i in com : 
        x,y = wall_list[i] 
        grid[x][y] = 0
    # for i in range(n) :
    #     print(grid[i])
    etime = bfs(start_x-1,start_y-1,grid)
    #print(etime)
    if etime : 
        min_elapsed_time = min(min_elapsed_time,etime)

if min_elapsed_time != MAX_VAL :
    print(min_elapsed_time)
else :
    print(-1)
