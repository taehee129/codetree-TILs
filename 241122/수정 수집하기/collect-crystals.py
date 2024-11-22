n,k = tuple(map(int,input().split()))

lst = input()

dp =[[0 for _ in range(k+1)] for _ in range(n)]

if lst[0] == "L" :
    dp[0][0] = 1
else :
    dp[0][1] = 1


# k%2==0 L  k%2== 1 R
for i in range(1,n) :
    for j in range(k+1) :

        if j == 0 :
            if lst[i] == 'L' :
                dp[i][j] = dp[i-1][j]+1
            else :
                dp[i][j] = dp[i-1][j]
        else :
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) 
            if (j%2 == 0 and lst[i] == "L" ) or (j%2 == 1 and lst[i]=="R") :
                dp[i][j] +=1
    
print(max(dp[n-1]))
