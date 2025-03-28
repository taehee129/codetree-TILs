n,m = map(int,input().split())

a = list(map(int,input().split()))
b= list(map(int,input().split()))

dp = [[[] for _ in range(m)] for _ in range(n)]


def dic(a,b) : 

    a_len = len(a)

    for i in range(a_len) : 

        if a[i]< b[i] :
            return a 
        if a[i] > b[i] :
            return b 
    return a

if a[0] == b[0] :
    dp[0][0] = [a[0]]

for i in range(1,m) : 
    dp[0][i] = dp[0][i-1][:] if a[0] != b[i] else [a[0]]

for i in range(1,n) :
    dp[i][0] = dp[i-1][0][:] if a[i] != b[0] else [b[0]] 


for i in range(1,n) : 
    for j in range(1,m) : 
        if a[i] == b[j] :
            lst = dp[i-1][j-1][:]
            lst.append(a[i])
            dp[i][j] = lst
        else : 
            lst1 = dp[i][j-1][:]
            lst2 = dp[i-1][j][:]

            if len(lst1) == len(lst2) and len(lst2) != 0 :
                dp[i][j] = dic(lst1, lst2)
            else : 
                dp[i][j] = lst1 if len(lst1) > len(lst2) else lst2


    
print(' '.join(map(str, dp[n-1][m-1])))