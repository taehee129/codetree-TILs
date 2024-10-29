n,m = tuple(map(int,input().split())) 

lst = list(map(int,input().split()))


dp = [10001]*m 
for i in lst :
    dp[i-1] = 1

for i in range(m) :
    for j in range(n) :
        if i-lst[j] >= 0 :
            dp[i] = min(dp[i],dp[i-lst[j]]+1)



print(dp[m-1])