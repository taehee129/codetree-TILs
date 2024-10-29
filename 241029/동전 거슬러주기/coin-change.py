n,m = tuple(map(int,input().split())) 

lst = list(map(int,input().split()))


dp = [10001]*(m+1) 

dp[0] =1 
for i in range(1,m+1) :
    for j in range(n) :
        if i-lst[j] >= 0 :
            dp[i] = min(dp[i],dp[i-lst[j]]+1)


if dp[m] ==10001 :
    print(-1)
else :
    print(dp[m])