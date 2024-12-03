n,r,c = tuple(map(int,input().split()))
r-=1
c -=1
lst = [
    list(map(int,input().split()))
    for _ in range(n)
]

ans =[] 
ans.append((r,c))
def in_range(x,y,n) : 
    if (x<0 or x>=n) or (y<0 or y>=n) :
        return False 
    return True 


def move(x,y,lst) : 
    dx = [-1,1,0,0]
    dy = [0,0,-1,1] 

    maxVal = lst[x][y]
    retX= -1
    retY = -1
    for i in range(4) : 
        nx =x+dx[i] 
        ny = y+dy[i]

        if not in_range(nx,ny,n) :
            continue 
        
        if lst[nx][ny] > maxVal : 
            retX = nx
            retY = ny
            maxVal = lst[nx][ny]
            break
    
    return retX,retY



while True :
    r,c = move(r,c,lst) 
    if (r,c) == (-1,-1) :
        break

    ans.append((r,c))


for x,y in ans : 
    print(lst[x][y], end=" ")
    