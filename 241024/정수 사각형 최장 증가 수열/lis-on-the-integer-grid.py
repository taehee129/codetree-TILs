n = int(input())

lst = [
    list(map(int, input().split()))
    for _ in range(n)
]


dp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

answer = 1

def advance(x,y) :

    global n
    global answer
    if dp[x][y] != 0 :
        return dp[x][y]

    move = [(1,0),(0,1),(-1,0),(0,-1)]

  
    maxCnt =0
    for dx,dy in move :
        nx,ny = x+dx, y+dy

        if not (nx>=0 and nx < n and ny>=0 and ny<n) :
            continue
        
        if lst[x][y] >= lst[nx][ny] :
            continue

        maxCnt = max(advance(nx,ny), maxCnt)

    dp[x][y] = maxCnt+1
    answer = max(answer, maxCnt+1)

    return maxCnt+1


for i in range(n) :
    for j in range(n) :
        advance(i,j)


print(answer)