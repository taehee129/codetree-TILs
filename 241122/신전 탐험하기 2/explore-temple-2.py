# 1 층 1,2,3 
# 직전 층에서  

n= int(input())

lst =[
    list(map(int,input().split()))
    for _ in range(n)
]


dp =[
    [[0 for _ in range(3)] for _ in range(3)] for _ in range(n)
]



dp[0] = [[lst[0][0],0,0],[0,lst[0][1],0],[0,0,lst[0][2]]]


for i in range(1,n) :
    for j in range(3) :
        for k in range(3) :
            for x in range(3) :
                if j==x :
                    continue

                if dp[i-1][x][k] != 0 :
                     
                    dp[i][j][k] = max(dp[i][j][k] , dp[i-1][x][k]+lst[i][j]) 

answer= 0
for i in range(3) :
    for j in range(3) :
        if i==j :
            continue
        answer = max(answer, dp[n-1][i][j])

print(answer)