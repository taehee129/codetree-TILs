a= input()
b= input() 


lenA= len(a)
lenB = len(b)
dp = [[0 for _ in range(lenB)] for _ in range(lenA)]


if a[0] == b[0] : 
    dp[0][0] = 1


for i in range(1,lenA) : 
    if b[0] == a[i] :
        dp[i][0] = 1
    else :
        dp[i][0] = dp[i-1][0]

for i in range(1,lenB) :
    if a[0] == b[i] :
        dp[0][i] = 1 
    else :
        dp[0][i] = dp[0][i-1]


for i in range(1,lenA) :
    for j in range(1,lenB) :
        if a[i] == b[j] :
            dp[i][j] = dp[i-1][j-1] +1 
        else :
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])


print(dp[lenA-1][lenB-1])