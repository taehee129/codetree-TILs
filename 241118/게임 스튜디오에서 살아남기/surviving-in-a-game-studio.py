

n = int(input())

dp = [
    [
        [0,0,0]
        for _ in range(3)
    ] 
    for _ in range(n+1)
]

dp[1][0][1] = 1 
dp[1][1][0] = 1
dp[1][0][0] = 1

for i in range(2,n+1) :
    for j in range(3) :
        for k in range(3) :
            if j == 0:
                if k==0 :
                    dp[i][j][k] = sum(dp[i-1][j]) 
                else : 
                    dp[i][j][k] = dp[i-1][j][k-1]
            else :
                if k ==0 :
                    dp[i][j][k] = sum(dp[i-1][j])+sum(dp[i-1][j-1])
                else : 
                    dp[i][j][k] = dp[i-1][j][k-1] 


        
                
sumVal = 0

for i in dp[n] :
    for j in i :
        sumVal+=j

print(sumVal%(10**9+7))
    


            

