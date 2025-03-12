n,m = tuple(map(int,input().split()))


grid = [list(map(int,input().split())) for _ in range(n)]


def in_range(x,y) : 
    if x<0 or x>=n or y<0 or y>=m : 
        return False
    return True 

flag =0
visited = [[0 for _ in range(m)] for _ in range(n)]

q = [(0,0)]

dxs, dys = [1,0,-1,0],[0,1,0,-1]
while len(q) >0 : 
    x,y = q.pop()
    if (x,y) == (n-1,m-1) : 
        flag = 1 
        break

    for dx,dy in zip(dxs,dys) : 

        newx,newy = x+dx,y+dy

        if not in_range(newx,newy) : 
            continue 
        if grid[newx][newy] == 0 :
            continue 
        if visited[newx][newy] ==1: 
            continue

        q.insert(0,(newx,newy))
        visited[newx][newy] = 1

print(flag)