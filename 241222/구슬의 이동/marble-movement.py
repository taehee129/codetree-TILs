n,m,t,k = tuple(map(int,input().split()))
lst =[]

grid = [
    [0 for _ in range(n)] for _ in range(n)
]

mapper={
    "R" : 0,
    "D" : 1,
    "U" : 2, 
    "L" : 3
}
for i in range(m) : 
    l = input().split()
    r,c,d,v = tuple(l) 
    r = int(r) -1
    c = int(c) -1
    d = mapper[d]
    v = int(v)
    lst.append([r,c,d,v,i])

for i in range(n) :
    for j in range(m) :
        for v in lst :
            if int(v[0]) == i and int(v[1]) == j :
                grid[i][j]+=1 


def valid(x,y) : 
    if x<0 or x>=n or y<0 or y>=n :
        return False
    return True

def printGrid(grid) : 
    for lst in grid :
        print(" ".join(map(str,lst)))


def move(x,y,d,v) :
    xds, yds = [0,1,-1,0],[1,0,0,-1]    

    for _ in range(v) : 
        
        nx,ny = x+xds[d],y+yds[d]
        if not valid(nx,ny) :
            d =3-d 
        x,y = x+xds[d],y+yds[d]

    return x,y,d

def explode(grid,k,lst) :
    temp = []
    for i in range(n) :
        for j in range(n) :
            if grid[i][j] >k :
                temp.append([i,j])

    for i in temp :
        x,y = i[0],i[1]
        cnt = 0
        #printGrid(lst)
        for j in range(len(lst)-1,-1,-1) :
            if lst[j][0] == x and lst[j][1] == y : 
               
                del lst[j]
                cnt +=1 
            if cnt ==grid[x][y] - k :
                break
    
    return lst



lst.sort(key= lambda x:(x[3],x[4]),reverse=True)

for _ in range(t) : 
    grid = [
        [0 for _ in range(n)] for _ in range(n)
    ]
    newLst = []
    for l in lst :
        r,c,d,v,_ = tuple(l)
        x,y,d = move(r,c,d,v)
        grid[x][y] +=1
        newLst.append([x,y,d,v])

    lst = explode(grid,k,newLst)

# printGrid(grid)
# print(lst)
print(len(lst))