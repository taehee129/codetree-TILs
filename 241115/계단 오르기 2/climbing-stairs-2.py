n = int(input())

lst = list(map(int,input().split()))


dp = [[0,0,0]]*n

dp[0]= [lst[0],0,0]


for i in range(n) :
    val = lst[i]
    dp[i] = [max(dp[i-2])+val,dp[i-1][0]+val,dp[i-1][1]+val]


print(max(dp[n-1]))


