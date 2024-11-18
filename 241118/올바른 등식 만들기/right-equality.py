n,m = tuple(map(int,input().split()))

lst = list(map(int,input().split()))


dp =[
    [0 for _ in range(41)]
    for _ in range(n)
]

dp[0][lst[0]+20] = 1
dp[0][lst[0]*(-1)+20] =1


for i in range(1,n) :
    for j in range(41) :
        if j-lst[i]>=0 :
            dp[i][j] = dp[i-1][j-lst[i]]
        if j+lst[i] < 41 :
            dp[i][j] += dp[i-1][j+lst[i]]
    
    
print(dp[n-1][m+20])
            
            
        
        





