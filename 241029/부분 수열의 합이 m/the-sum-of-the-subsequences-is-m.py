n,m= tuple(map(int, input().split()))

lst = list(map(int,input().split()))

maxNum = 10001
dp = [
    [maxNum]*(m+1) 
    for _ in range(n)
]


for i in range(n) : 
    if lst[i] <= m :
        dp[i][lst[i]] =1

for i in range(1,n) :
    for j in range(1,m+1) :
        
        if j-lst[i] > 0 :
            dp[i][j] = min(dp[i-1][j-lst[i]]+1, dp[i-1][j])
        else :
            dp[i][j] = min(dp[i][j], maxNum)


asw = maxNum
for i in range(n) :
    #print(dp[i])
    asw = min(dp[i][m],asw)

if asw == maxNum :
    print(-1)
else :
    print(asw)