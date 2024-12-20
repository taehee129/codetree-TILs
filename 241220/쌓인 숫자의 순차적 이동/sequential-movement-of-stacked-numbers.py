

# 움직일 숫자의 매트릭스 위치값
# 움직일 숫자의 리스트 위치값
# 최대값의 위치 


n,m =  tuple(map(int,input().split()))

grid = [
    [[] for _ in range(n)] for _ in range(n)
]
for i in range(n) :
    lst = list(map(int,input().split()))
    for j in range(n) :
        
        grid[i][j].append(lst[j])

change = list(map(int,input().split()))

def valid(x,y) : 
    if x<0 or x>=n or y<0 or y>=n : 
        return False
    return True 

def findGridIdx(num,grid) : 
    for i in range(n) :
        for j in range(n) :
            for idx,k in enumerate(grid[i][j]) :
                if k == num :
                    return i,j, idx
    return False

def findMax(x,y,grid) : 
    dxs,dys = [1,-1,0,0,1,-1,1,-1],[0,0,1,-1,1,-1,-1,1]
    maxNum=0
    rx,ry = -1,-1
    for dx,dy in zip(dxs,dys) :
        nx,ny = x+dx,y+dy 
        if not valid(nx,ny) : 
            continue 
        for i in grid[nx][ny] :
            if i >maxNum :
                maxNum= i
                rx,ry = nx,ny
    return rx,ry 


def printGrid(grid) :
    for i in grid :
        print(i)
    print()


for num in change :
    newGrid = [[[] for _ in range(n)]for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            newGrid[i][j] = grid[i][j][:]


    x,y,idx = findGridIdx(num,grid)
    rx,ry = findMax(x,y,grid)

    
    if rx ==-1 :
        continue

    # printGrid(grid)
    # printGrid(newGrid)
    # print(x,y,rx,ry)
    newGrid[x][y] = grid[x][y][0:idx]
    newGrid[rx][ry] = grid[rx][ry] + grid[x][y][idx:]


    grid = newGrid 
    #printGrid(grid)


for i in range(n) :
    for j in range(n) :
        if len(grid[i][j]) ==0 :
            print(None)
            continue
        for k in range(len(grid[i][j])-1,-1,-1) :
            print(grid[i][j][k],end=" ")
        
        print()
        



        