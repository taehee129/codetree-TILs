n,m= tuple(map(int,input().split()))

lst = list(map(int,input().split()))

dp = [-1]*(m+1)

dp[0] =0

for i in range(m+1) :
    for j in range(n) :
        if i-lst[j] >= 0 and dp[i-lst[j]] !=-1:
            dp[i] = max(dp[i],dp[i-lst[j]]+1)

print(dp[m])