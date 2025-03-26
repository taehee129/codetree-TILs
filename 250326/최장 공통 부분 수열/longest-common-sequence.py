a = input()
b = input()

n = len(a)
m = len(b)

dp = [[0 for _ in range(m)] for _ in range(n) ]


if a[0] == b[0] :
    dp[0][0] = 1 

for i in range(1,m) : 
    dp[0][i] = max(dp[0][i-1], 1 if a[0] == b[i] else 0)
for i in range(1,n) : 
    dp[i][0] = max(dp[i-1][0], 1 if a[i] == b[0] else 0)

for i in range(1,n) :
    for j in range(1,m) : 
        dp[i][j] = max(dp[i-1][j],dp[i][j-1], dp[i-1][j-1] +1 if a[i] == b[j] else 0)

# for lst in dp :
#     print(' '.join(map(str,lst)))

print(dp[n-1][m-1])
   