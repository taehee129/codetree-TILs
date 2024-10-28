n = int(input())


lst = list(map(int, input().split()))

dp = [0]*n


for i in range(n) :
    for j in range(0,i) :
        if lst[j]+j < i : 
            continue
        dp[i] = max(dp[i], dp[j]+1)


print(max(dp))