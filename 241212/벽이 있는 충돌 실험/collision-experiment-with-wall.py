def valid(x,y) : 
    global n 

    if x<0 or x>=n or y<0 or y>=n :
        return False
    
    return True 

mapper = {
    "U" : 1 ,
    "R" : 2 ,
    "L" : 3 ,
    "D" : 4
}

def move(x,y,d) : 
    
    dx,dy = [-1,0,0,1],[0,1,-1,0]

    nx,ny = x+dx[d],y+dy[d]

    if not valid(nx,ny) :
        d = 3-d
        return x,y,d

    return nx,ny,d

    

def tern(gird,dGrid) : 
    global n 
    newGrid = [
        [0 for _ in range(n)] for _ in range(n)
    ]
    newd = [
        [0 for _ in range(n)] for _ in range(n)
    ]
    for i in range(n) : 
        for j in range(n) : 
            if grid[i][j] != 1 :
                continue 
            d = dGrid[i][j]

            x,y,d = move(i,j,d-1)
            newGrid[x][y] +=1 
            newd[x][y] = d+1 
    
    return newGrid,newd
                
def explosion(gird,dGrid) :
    global n 
    for i in range(n) : 
        for j in range(n) :
            if grid[i][j] >=2 : 
                grid[i][j] =0
                dGrid[i][j] = 0
    return grid,dGrid

def printGrid(grid) :
    for lst in grid :
        print(" ".join(map(str,lst)))
    print()


t = int(input())
for _ in range(t) : 
    n,m = tuple(map(int,input().split()))
    grid = [
        [0 for _ in range(n)] for _ in range(n)
    ]
    dGrid = [
        [0 for _ in range(n)] for _ in range(n)
    ]
    for _ in range(m) : 
        x,y,d = tuple(input().split())
        x = int(x)-1 
        y = int(y)-1
        d = mapper[d]

        grid[x][y] = 1 
        dGrid[x][y] = d
    
    for _ in range(n*2) : 
     
        
        grid ,dGrid = tern(grid,dGrid)
        grid, dGrid = explosion(grid,dGrid) 
        # printGrid(grid)
        # printGrid(dGrid)

    cnt = 0
    for i in range(n) : 
        for j in range(n) :
            if grid[i][j] ==1 :
                cnt+=1
    print(cnt)


