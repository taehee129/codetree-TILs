n= int(input())

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]




# 1  D -> L , U-> R , R->U,L->D 
# 2  D -> R,  U ->L , R->D,L->U

dx,dy = [1,-1,0,0],[0,0,1,-1]
#  D U R L 

mapper = {
    "D" : 0 ,
    "U" : 1,
    "R" : 2,
    "L" : 3
}

def valid(x,y) :
    if x<0 or x>=n or y<0 or y>=n :
        return False
    return True


def move(x,y,d) : 

    if valid(x,y) and grid[x][y]==1 :
        d = (3-d)
    
    elif valid(x,y) and grid[x][y] ==2 :
        if d == 0 :
            d = 2
        elif d ==2 :
            d= 0
        elif d==1 :
            d=3
        elif d==3:
            d =1
        
    x,y = x+dx[d],y+dy[d]

    return x,y,d

def game(x,y,d) : 
    t = 0
    while True : 
        x,y,d = move(x,y,d)
        t +=1

        if not valid(x,y) :
            return t

ans =0
for i in range(n) : 
    (x,y,d) = (-1,i,0)
    ans= max(ans,game(x,y,d))

for i in range(n) : 
    (x,y,d) = (n,i,1)
    ans= max(ans,game(x,y,d))

for i in range(n) : 
    (x,y,d) = (i,-1,2)
    ans= max(ans,game(x,y,d))

for i in range(n) : 
    (x,y,d) = (i,n,3)
    ans= max(ans,game(x,y,d))

print(ans)