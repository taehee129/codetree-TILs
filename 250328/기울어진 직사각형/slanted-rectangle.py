n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]

dxy = [(-1,1),(-1,-1),(1,-1),(1,1)]

x,y =1,1 

def in_range(x,y) : 
    if x<0 or x>=n or y<0 or y>=n : 
        return False
    return True
    
def rect(r,c,x,y) : 
    sum_val = 0
    for i in range(x) : 
        r,c = r-1,c+1
        if not in_range(r,c) :
            return False
        sum_val += grid[r][c]

    for i in range(y) : 
        r,c = r-1,c-1
        if not in_range(r,c) :
            return False
        sum_val += grid[r][c]
    for i in range(x) : 
        r,c = r+1,c-1
        if not in_range(r,c) :
            return False
        sum_val += grid[r][c]
    for i in range(y) : 
        r,c = r+1,c+1
        if not in_range(r,c) :
            return False
        sum_val += grid[r][c]
    return sum_val 



max_val =0
for i in range(n) :
    for j in range(n) : 
        for x in range(1,n) :
            for y in range(1,n) : 
                val = rect(i,j,x,y)
                if val :
                    max_val = max(val,max_val)
                else :
                    break
        
print(max_val)