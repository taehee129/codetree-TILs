n= int(input())

lst = list(map(int,input().split()))


dp = [0]*(n+1)


for i in range(1,n+1) :
    for j in range(1,n+1) :
        val = j-i 
        if val > 0 and dp[val]>0 :
            dp[j] = max(dp[j], dp[val]+lst[i-1])
        elif val == 0 :
            dp[j] = max(dp[j], lst[i-1])


print(max(dp))