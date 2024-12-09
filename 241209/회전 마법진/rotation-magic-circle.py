# 111
# 323 

# n 자리 수 숫자가 m 번 반대쪽으로 회전할 때의 최솟 값 dp[n][m]

n= int(input())

orgin = input()

goal = input()


def left(x,g) :
    for i in range(10) :
        if (x+i)%10 == g :
            return i 


def right(x,g) :
    for i in range(10) :
        if (x-i)%10 == g:
            return i
    pass 


def m(x,g) : 
 
    
    return min(left(x,g), right(x,g))

dp = [
    [10000000 for _ in range(10)] for _ in range(len(orgin))
]

end = len(orgin)-1
for i in range(10) :
    val = int(orgin[end])
    g = int(goal[end])
    
    val = (val+i)%10            
   
    dp[0][i] = i+min(left(val,g),right(val,g))



for i in range(1,end+1) :
    for j in range(10) :
        # for k in range(j,10) :
        #     val = int(orgin[end-i])
        #     g = int(goal[end-i])

        #     val = (val+k)%10   
        #    # print(i,j,min(val,g))  
        #     dp[i][j] = min(dp[i][j],dp[i-1][j] +min(val,g)) 
        val = int(orgin[end-i])
        g = int(goal[end-i])
        val = (val+j)%10
        dp[i][j] = min(dp[i][j],dp[i-1][j] +right(val,g))

# for i in dp :
#     print(i)  
 
ans = 1000000
for i in range(10) :
    ans = min(ans, dp[n-1][i])

print(ans)
#     5    