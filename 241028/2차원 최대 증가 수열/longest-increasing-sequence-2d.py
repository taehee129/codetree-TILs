n,m = tuple(map(int,input().split()))

lst = [
    list(map(int,input().split()))
    for _ in range(n)
]



dp =[
    [1]*m 
    for _ in range(n)
]

asw =0
for i in range(n) :
    for j in range(m) :
        for x in range(i) :
            for y in range(j) :
                if not (x==0and y==0) and dp[x][y] ==1 :
                    continue

                if lst[i][j] > lst[x][y] :
                    dp[i][j] = max(dp[i][j], dp[x][y]+1)
                    asw = max(dp[i][j], asw)

print(asw)