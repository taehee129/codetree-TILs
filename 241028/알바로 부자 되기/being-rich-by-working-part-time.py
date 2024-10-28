n= int(input()) 

lst =[
    list(map(int,input().split()))
    for _ in range(n)
]


lst.sort(key=lambda x : x[0])

dp =[ val[2] for val in lst] 


for i in range(n) :
    for j in range(i) :
        if lst[i][0] > lst[j][1] :
            dp[i] =max(dp[i], dp[j]+lst[i][2])

print(max(dp))