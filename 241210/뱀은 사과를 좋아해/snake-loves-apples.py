n,m,k = tuple(map(int,input().split()))

grid = [
    [ 0 for _ in range(n)] for _ in range(n)
]



snake = [[0,0]]
length = 1 
second = 0

dx,dy = [1,-1,0,0],[0,0,1,-1]
mapper = {
    "D" : 0,
    "U" : 1, 
    "R" :2 ,
    "L" : 3
}

history = [
    [0 for _ in range(n)] for _ in range(n)
]

def checkEnd(history) :
    for i in range(n) :
        for j in range(n) : 
            if history[i][j] ==0 :
                return False
    return True
def move(snake, d) :
    global second
    global length
    x,y = tuple(snake[length-1])
    x,y = x+dx[mapper[d]], y +dy[mapper[d]]
    second +=1

    if [x,y] in snake :
        # print(x,y)
        return False 
    
    if x<0 or x>=n or y<=0 or y>=n :
        return False 
    snake.append([x,y])
    history[x][y] =1
    if grid[x][y] != 1 :
        snake= snake[1:]
    else :
        length +=1
   
    return snake

for _ in range(m) :
    x,y = tuple(map(int,input().split()))
    x-=1
    y-=1
    grid[x][y] =1

# 전부 움직였거나, 겹치거나 , 격자를 벗어낫거나 
# for lst in grid :
#     print(lst)
endFlag = False
for _ in range(k) :
    d,p = tuple(input().split())
    p = int(p)
    for _ in range(p) :

        snake = move(snake,d)
        #print(snake)
        if not snake :
            endFlag =True

            break
        if checkEnd(history) :
            endFlag =True

            break
    if endFlag :
        break

print(second)