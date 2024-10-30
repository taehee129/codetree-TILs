n,m= tuple(map(int,input().split()))

lst = list(map(int,input().split()))

dp = [0]*(m+1)

for i in range(n) :
    for j in range(m,-1,-1) :
        val = j-lst[i]

        if val >0 and dp[val] !=0 :
            dp[j] = 1
        elif val == 0 :
            dp[j] =1

if dp[m] ==1 :
    print('Yes')
else :
    print('No')