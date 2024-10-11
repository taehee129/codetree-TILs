def in_range(par, ran) : 
    if par <0 or par >= ran :
        return False 
    return True 


n,m = tuple(map(int, input().split()))

mat = [
    list(map(int, input().split()))
    for _ in range(n)

]




def cal1(x,y) : 
    maxVal =0
    dx, dy = [-1,0,1,0], [0,1,0,-1]
    for i in range(4) : 
        a,b  = x+dx[i] , y+dy[i] 
        a2,b2 = x+dx[(i+1)%4] , y+dy[(i+1)%4]
        if in_range(a,n) and in_range(b,m) and in_range(a2,n) and in_range(b2,m) : 
           
            maxVal = max(maxVal,  mat[x][y] + mat[a][b] + mat[a2][b2])
    
    return maxVal
    


def cal2(x,y) :
    maxVal =0
    dx, dy = [-1,0,0,1], [0,1,-1,0]

    for i in range(2) : 
        a,b = x+dx[i] , y+dy[i]
        a2,b2 = x+dx[3-i] , y+dy[3-i] 
        if in_range(a,n) and in_range(b,m) and in_range(a2,n) and in_range(b2,m) : 
            
            maxVal = max(maxVal,  mat[x][y] + mat[a][b] + mat[a2][b2])
    
    return maxVal



ret = 0
for i in range(n) : 
    for j in range(m) : 
        ret =  max(ret, max(cal1(i,j), cal2(i,j)))

print(ret)