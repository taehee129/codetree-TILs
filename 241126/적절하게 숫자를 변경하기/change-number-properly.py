n,m = tuple(map(int,input().split()))

lst= list(map(int,input().split()))
m+=1
dp = [
       [
            [0            
            for _ in range(4)            
            ] 
        for _ in range(m)
        ]
    for _ in range(n)
    ]


dp[0][0][lst[0]-1] =1 
answer=1

# m 다른 횟수 
#dp[n][m][k] = 1.dp[n-1][m] or 2.dp[n-1][m-1]
#           1. dp[n-1][m][k] lst[n] =k 라면 +1 
#           2. dp[n-1][m-1][~k] lst[n]= ~k 라면 +1 중에서 최대값 

for i in range(1,n) :
    for j in range(m) :
        for k in range(4) :
            maxVal = 0
            maxVal = max(maxVal, dp[i-1][j][k]+ (1 if (k+1) ==lst[i] else 0))

            for x in range(4) :
                if j ==0 :
                    break
                if x ==k :
                    continue 
                maxVal =max(maxVal, dp[i-1][j-1][x] +(1 if (k+1)==lst[i] else 0))
        
            dp[i][j][k] = maxVal
            answer = max(answer,maxVal)
        


print(answer)

