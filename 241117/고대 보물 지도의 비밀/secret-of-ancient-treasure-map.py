n,k = tuple(map(int,input().split()))

lst = list(map(int, input().split()))

minVal = -100000
maxVal = minVal
dp=[
    [minVal for _ in range(k+1)]
    for _ in range(n)
    ]


if lst[0] >= 0 :
    dp[0][0] = lst[0]
if lst[0] <0 :
    
    dp[0][1] = lst[0]
maxVal= lst[0]
for i in range(1,n) : 
    for j in range(k+1) :
        if lst[i] >= 0 :
            dp[i][j] = max(lst[i], dp[i-1][j]+lst[i])
        else :
            if j==0 :
                dp[i][j] = minVal
                continue
            dp[i][j] = max(lst[i], dp[i-1][j-1]+lst[i])
        maxVal = max(dp[i][j], maxVal)
    



print(maxVal)

            

        


