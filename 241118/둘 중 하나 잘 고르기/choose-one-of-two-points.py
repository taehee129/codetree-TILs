n= int(input())

lst = [
    list(map(int,input().split()))
    for _ in range(2*n)
]


dp = [[0 for _ in range(n+1)] for _ in range(n+1)]



dp[1][0] = lst[0][0]
dp[0][1] = lst[0][1]

for i in range(1,n+1) :
    dp[i][0] = dp[i-1][0] +lst[i-1][0]
    dp[0][i] = dp[0][i-1] + lst[i-1][1]
for i in range(1,n+1) :
    for j in range(1,n+1) : 
        dp[i][j] = max(dp[i-1][j]+ lst[i+j-1][0], dp[i][j-1]+ lst[i+j-1][1]) 

print(dp[n][n])

        
        