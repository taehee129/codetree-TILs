n = int(input())

lst =[1,2,5]

dp = [0]*(n+1)

dp[0] = 0

for i in range(1,n+1) :
    for j in lst :
        if i-j > 0 :
            dp[i] += dp[i-j]
        if i==j :
            dp[i] +=1 


print(dp[n])