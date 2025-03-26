a = input()
b = input()


n = len(a)
m = len(b)

import sys
MAX_VAL = sys.maxsize

dp = [[ MAX_VAL for _ in range(m)] for _ in range(n)]


if a[0]==b[0] :
    dp[0][0] = 0
else :
    dp[0][0] = 1 


for i in range(1,m) : 
    dp[0][i] = dp[0][i-1] +1 if a[0] != b[i] else i 
    
for i in range(1,n) : 
    dp[i][0] = dp[i-1][0] +1 if a[i] != b[0] else i


for i in range(1,n) : 
    for j in range(1,m) : 
        if a[i] == b[j] : 
            dp[i][j] = dp[i-1][j-1]
        else : 
            dp[i][j] = min(dp[i-1][j],dp[i][j-1]) +1



print(dp[n-1][m-1])