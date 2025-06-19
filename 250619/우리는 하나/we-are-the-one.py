n,k,u,d = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]

def check(a,b) : 
    if a< 0 or a>=n or b<0 or b>=n :
        return False
    return True

trace = [[0 for _  in range(n)] for _ in range(n)]

def dfs(a,b) : 
    q = [] 
    q.append((a,b))
    trace[a][b] = 1
    dxs,dys = [0,1,0,-1],[1,0,-1,0]
    cnt =1 
    #print(a,b)
    while q :
        #print(q)
        x,y = q.pop()
        for dx,dy in zip(dxs,dys) : 
            nx,ny =x+dx,y+dy 

            if not check(nx,ny) : 
                continue                
            if trace[nx][ny] ==1 : 
                continue
            dif = abs(grid[x][y]-grid[nx][ny] )
            
            if dif >= u and dif<= d :
                q.insert(0,(nx,ny))
                cnt +=1 
                trace[nx][ny] =1 

    return cnt 

lst = []

for i in range(n) :
    for j in range(n) :
        if trace[i][j] == 1 :
            continue
        lst.append(dfs(i,j))

lst.sort(reverse=True)               
cnt = 0 

for i in range(k) :
    cnt +=lst[i]

print(cnt)

        