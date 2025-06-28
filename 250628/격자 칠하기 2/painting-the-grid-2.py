n = int(input())
origin_grid = [list(map(int,input().split())) for _ in range(n)]

def in_range(x,y) : 
    if x<0 or x>=n or y<0 or y>=n :
        return False 
    return True

def check(x,y,d) : 
    
    dxs,dys = [0,1,0,-1],[1,0,-1,0]

    global visited

    q = [(x,y)]
    cnt =0
    while q :
        x,y = q.pop()

        for dx,dy in zip(dxs,dys) :
            nx,ny = x+dx,y+dy

            if not in_range(nx,ny) :
                continue 
            if visited[nx][ny] : 
                continue 
            #print(abs(origin_grid[x][y]-origin_grid[nx][ny]), d)
            if abs(origin_grid[x][y]-origin_grid[nx][ny]) <=d :
                visited[nx][ny] = 1 
                q.append((nx,ny))
                cnt +=1 
    
    return cnt


left = 0 
right = 1000000
ans = 1000000 

while left <= right : 
    mid = (left+right)//2
    
    visited = [[0 for _ in range(n)] for _ in range(n)]
    flag = False
    for i in range(n) :
        for j in range(n) :
            if visited[i][j] == 1 :
                continue 
            a = n**2 

            if a%2 == 1 :
                a = a+1 

            if check(i,j,mid) >=a/2 : 
                flag = True 
                break
    if flag : 
        right = mid-1 
        ans = min(ans,mid)
    else :
        left = mid +1

print(ans)
# visited = [[0 for _ in range(n)] for _ in range(n)]
# print(check(0,0,3))        

