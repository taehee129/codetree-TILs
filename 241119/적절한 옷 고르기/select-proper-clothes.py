n,m = tuple(map(int,input().split()))



lst  = [
    list(map(int,input().split()))
    for _ in range(n)
]



dp = [
    [0 for _ in range(n)] for _ in range(m)
]



for i in range(1,m) :
    

    for j in range(n) :
        maxVal=0
        if lst[j][0] <= i+1 and lst[j][1] >= i+1 :
            for k in range(n) :
                if lst[k][0] <= i and lst[k][1] >= i :
                    maxVal = max(maxVal, abs(lst[j][2]-lst[k][2])+dp[i-1][k])
            
            dp[i][j] = maxVal
    
    




print(max(dp[m-1]))            