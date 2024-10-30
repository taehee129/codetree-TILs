n,m = tuple(map(int,input().split()))

lst = [
    tuple(map(int,input().split()))
    for _ in range(n)
]


dp = [0]*(m+1)

for i in range(n) :
    for j in range(m,-1,-1) :
        val = j-lst[i][0]

        if val > 0 and dp[val] >0 :
            dp[j] =max(dp[j],dp[val]+lst[i][1])
        elif  val == 0 :
            dp[j] = max(dp[j],lst[i][1])


print(max(dp))