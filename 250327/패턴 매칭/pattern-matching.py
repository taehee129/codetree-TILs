s = input()
p = input()


n,m = len(s), len(p)

dp = [[False for _ in range(m)] for _ in range(n)]

if p[0] == '.' or p[0] == s[0] :
    dp[0][0] = True 

if len(p) >=2 and p[1] =='*' :
    dp[0][1] = True


for i in range(1,n) :
    for j in range(1,m) :
        if p[j] == '*' and dp[i-1][j] == True and s[i] == s[n-1]  :
            dp[i][j] = True 
        elif p[j] == '.' and dp[i-1][j-1] == True :
            dp[i][j] = True 
        elif p[j] == s[i] and dp[i-1][j-1] == True :
            dp[i][j] = True
         
if dp[n-1][m-1] or p=='.*':
    print('true')
else : 
    print('false')