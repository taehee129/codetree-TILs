n,m,t = tuple(map(int,input().split()))

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

bomb = [
    [0 for _ in range(n)] for _ in range(n)
]


for _ in range(m) :
    x,y = tuple(map(int,input().split()))

    x-=1
    y-=1
    bomb[x][y] = 1


def valid(x,y) :
    if x<0 or x>=n or y<0 or y>=n :
        return False
    return True 


def explosion(x,y) : 
    retx,rety=(0,0)
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    maxVal=0
    for i in range(4) :
        newx,newy = x+dx[i],y+dy[i]
        if valid(newx,newy) and maxVal < grid[newx][newy] :
            maxVal = grid[newx][newy]
            retx,rety = (newx,newy)

    return retx,rety 



for _ in range(t) : 
    newBomb = [
        [0 for _ in range(n)] for _ in range(n)
    ]
    for i in range(n) :
        for j in range(n) : 
            if bomb[i][j] ==1 : 
                x,y = explosion(i,j)
                newBomb[x][y] +=1 
                if newBomb[x][y]>=2 :
                    newBomb[x][y]= 0
    bomb = [
        lst[:] for lst in newBomb
    ]

    # for lst in bomb :
    #     print(lst)
    # print()
cnt =0 

for i in range(n) :
    for j in range(n) :
        if bomb[i][j] == 1 :
            cnt +=1

print(cnt)