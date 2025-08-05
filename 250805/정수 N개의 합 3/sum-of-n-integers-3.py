n,k = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

prefix = [[0]*(n+1) for _ in range(n+1)]



for i in range(1,n+1)  :
    for j in range(1,n+1) :
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]+ arr[i-1][j-1]

ans = 0
for i in range(1+(k-1),n+1) : 
    for j in range(1+(k-1), n+1) :
        ans = max(ans, prefix[i][j] - prefix[i-k][j]-prefix[i][j-k]+ prefix[i-k][j-k])

print(ans) 
