n= int(input())

grid = [list(map(int,input().split())) for _ in range(n)]

direction = [list(map(int,input().split())) for _ in range(n)]

dxs,dys = [-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]

def in_range(x,y) : 
    if x<0 or x>=n or y<0 or y>=n : 
        return False
    return True

def max_move(x,y) :
    max_val = 0
    d = direction[x][y]-1
    dx,dy = dxs[d],dys[d]

    #print('-'*20+str(x)+str(y)+'-'*20)

    for i in range(1,n) : 
        nx,ny = x+dx*i,y+dy*i
        #print(nx,ny)
        if not in_range(nx,ny) : 
            break 
        if grid[x][y] >= grid[nx][ny] : 
            continue
        max_val= max(max_move(nx,ny)+1 , max_val)
    
    return max_val

start_x,start_y = map(int,input().split())

print(max_move(start_x-1,start_y-1))
    
    


    
    