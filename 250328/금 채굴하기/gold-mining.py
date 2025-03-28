n,m = map(int, input().split())
gold_grid = [list(map(int,input().split())) for _ in range(n)]

def in_range(x,y) : 
    if x<0 or x>=n or y<0 or y>=n :
        return False
    return True

def bfs(lst,grid) : 

    ret_lst = []
    dxs, dys = [1,0,-1,0],[0,1,0,-1]

    for x,y in lst : 
        for dx,dy in zip(dxs,dys) : 
            nx,ny = x+dx,y+dy 
            if not in_range(nx,ny) :
                continue 
            if grid[nx][ny] == 1 : 
                continue 
            grid[nx][ny] =1 
            ret_lst.append((nx,ny))
    
    return ret_lst, grid

def count_gold(gold_grid, dig_grid) : 
    cnt = 0
    for i in range(n) :
        for j in range(n) :
            if gold_grid[i][j] ==1 and dig_grid[i][j] ==1 :
                cnt+=1 
    
    return cnt


max_cnt = 0

for i in range(n) :
    for j in range(n) :
        k=0
        lst = [(i,j)]
        dig_grid = [[0 for _ in range(n)] for _ in range(n)]
        dig_grid[i][j] = 1
        while len(lst) >=1 :
            cnt = count_gold(gold_grid,dig_grid)
            # if max_cnt < cnt*m - (k**2+(k+1)**2) :
            #     print(lst)
            #     for l in dig_grid :
            #         print(l)
            #     print(k,cnt)
            if cnt*m - (k**2+(k+1)**2) >=0 :
                max_cnt = max(cnt,max_cnt)
            lst , dig_grid = bfs(lst,dig_grid)
            k+=1

print(max_cnt)









    
