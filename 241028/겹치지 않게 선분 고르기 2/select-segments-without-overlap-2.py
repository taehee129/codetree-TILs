n = int(input())

lst = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

dp = [1]*n

lst.sort(key = lambda x : x[0])

for i in range(n) :
    for j in range(i) :

        if lst[j][1] <lst[i][0] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))