n = int(input())
lst = list(map(int, input().split()))


dp = [1]*n

dp2 =[1]*n

for i in range(n) :
    for j in range(i) :
        if lst[i]>  lst[j] :
            dp[i] = max(dp[i], dp[j]+1)

lst2 = [1]*n

for i in range(n) :
    lst2[i] = lst[n-1-i]

for i in range(n) :
    for j in range(i) :
        if lst2[i]>  lst2[j] :
            dp2[i] = max(dp2[i], dp2[j]+1)

aswLst =[1]*n


for i in range(n) :
    aswLst[i] = dp[i]+dp2[n-1-i] -1 
# print(lst)
# print("lst2 : "+str(lst2))
# print(dp)
# print(dp2)
# print(aswLst)
print(max(aswLst))