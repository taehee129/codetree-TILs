n,m = tuple(map(int,input().split())) 

lst = list(map(int,input().split()))


dp = [10001]*(m+1) 

dp[0] =0

for i in range(n) :
    for j in range(1,m+1) :
        if (j-lst[i]) >=0 :
            dp[j] = min(dp[j], dp[j-lst[i]]+1)
            


if dp[m] ==10001 :
    print(-1)
else :
    print(dp[m])