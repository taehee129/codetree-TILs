a = input()
b= input()

n,m = len(a), len(b)

dp = [['' for _ in range(m)] for _ in range(n)]


if a[0] == b[0] : 
    dp[0][0] += a[0]


for i in range(1,m) : 
    dp[0][i] = dp[0][i-1]

    if a[0] == b[i] :
        dp[0][i] = a[0]

for i in range(1,n) : 
    dp[i][0] = dp[i-1][0]

    if a[i] == b[0] :
        dp[i][0] = a[i]

for i in range(1,n) : 
    for j in range(1,m) : 
        if a[i] == b[j] : 
            dp[i][j] = dp[i-1][j-1] + a[i]
        else : 
            dp[i][j] = dp[i-1][j] if len(dp[i-1][j]) >= len(dp[i][j-1]) else dp[i][j-1]


for lst in dp :
    print(lst)

print(dp[n-1][m-1])