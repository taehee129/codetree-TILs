n,m = tuple(map(int,input().split()))

grid = [
    list(map(int,input().split())) for _ in range(n)
]

def printGrid(grid) :
    for lst in grid :
        print(' '.join(map(str,lst)))
    print()

def valid(x,y) : 
    if x<0 or x>=n or y<0 or y>=n :
        return False
    return True

def swap(x,y,grid) : 
    newGrid = [
        lst[:] for lst in grid 
    ]

    dxs,dys = [1,-1,0,0,1,-1,1,-1],[0,0,1,-1,1,1,-1,-1]
    maxVal = 0
    retx,rety = (0,0)
    for dx,dy in zip(dxs,dys) : 
        newx ,newy = x+dx,y+dy
        if valid(newx,newy) and maxVal < grid[newx][newy] : 
            maxVal = grid[newx][newy]
            retx,rety = (newx,newy)
    newGrid[retx][rety] = grid[x][y]
    newGrid[x][y] = grid[retx][rety]
    #print(x,y,retx,rety)
    #printGrid(newGrid)
    return newGrid 


def tern(grid) :
    for num in range(n**2) : 
        flag =False
        for i in range(n) :
            for j in range(n) :
                if grid[i][j] == (num+1) :
                    grid = swap(i,j,grid)
                    flag = True 
                    break
                  
            if flag :
                break

        #printGrid(grid)

    return grid

for _ in range(m) : 
    grid = tern(grid)

printGrid(grid)