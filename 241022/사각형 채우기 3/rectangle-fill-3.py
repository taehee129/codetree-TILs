n= int(input())


dp = [
    0 for _ in range((n if n>=4 else 4))
]
dp[0] = 2 
dp[1] =7 
dp[2] = 22
dp[3] = 71

for i in range(4,n) :
    #dp[i] = dp[i-1]*2 + dp[i-2]*3 + dp[i-3]*2 +dp[i-4]*2+dp[i-5]*2+dp[i-6]*2+2

    x =0 
    for j in range(i) :
        x += dp[j]*(2 if j != i-2 else 3)
    
    dp[i] = x+2


print(dp[n-1]%1000000007)