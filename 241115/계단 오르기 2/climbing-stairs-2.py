n = int(input())

lst = list(map(int,input().split()))


dp = [[0,0,0,0] 
    for _ in range(n)
]

dp[0]= [0,lst[0],0]
dp[1] = [lst[1], 0, lst[0]+lst[1]]
for i in range(2,n) :
    val = lst[i]
    # dp[i] = [max(dp[i-2])+val,dp[i-1][0]+val,dp[i-1][1]+val,dp[i-1][2]+val]
    dp[i][0] = max(dp[i-2])+val

    for j in range(2) :
        if dp[i-1][j] != 0 :
           
            dp[i][j+1] = dp[i-1][j]+val





print(max(dp[n-1]))


371196