n = int(input())

lst = list(map(int,input().split()))


dp = [[0,0,0,0] 
    for _ in range(n)
]

dp[0]= [0,lst[0],0,0]
dp[1] = [lst[1], 0, lst[0]+lst[1],0]
for i in range(2,n) :
    val = lst[i]
    
    dp[i][0] = dp[i-2][0]+val

    for j in range(3) :
        maxVal = max(dp[i-1][j],dp[i-2][j+1])
        if maxVal != 0 :
            dp[i][j+1] =maxVal+val

    # dp[i][1] = max(dp[i-1][0],dp[i-2][1])+val
    # dp[i][2] = max(dp[i-1][1],dp[i-2][2])+val
    # dp[i][3] = max(dp[i-1][2],dp[i-2][3])+val



print(max(dp[n-1]))

# dp


