n = int(input())


lst = list(map(int,input().split()))

dp = [1 for _ in range(n)]


for i in range(1,n) :
    for j in range(0,i):
        if lst[j] < lst[i] :
            dp[i] = max(dp[i] , dp[j]+1)
            
        


print(max(dp))