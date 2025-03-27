s = input()
p = input()


n,m = len(s), len(p)

dp = [[False for _ in range(m)] for _ in range(n)]

if p[0] == '.' or p[0] == s[0] :
    dp[0][0] = True 

for i in range(1,m) : 
    if p[i] == '*' :
        dp[0][i] = dp[0][0]

for i in range(1,n) :
    for j in range(1,m) :
        if p[j] == '*' :
            if (s[i] == p[j-1] or p[j-1] =='.') and (dp[i-1][j] == True or dp[i-1][j-2] ==True) : 
                dp[i][j] = True 
            if s[i] != p[j-1] and dp[i][j-2] == True:
                dp[i][j]= True
        elif p[j] == '.' and dp[i-1][j-1] == True :
            dp[i][j] = True 
        elif p[j] == s[i] and dp[i-1][j-1] == True :
            dp[i][j] = True


# for lst in dp : 
#     print(lst)
if dp[n-1][m-1]:
    print('true')
else : 
    print('false')