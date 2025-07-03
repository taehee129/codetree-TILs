n,k = map(int,input().split())

nums = list(map(int,input().split()))


d ={}

for num in nums :
    if num in d : 
        d[num] +=1 
    else :
        d[num] =1 

cnt =0
for num in nums : 
    diff = k-num 
    if diff in d :
        cnt += d[diff]
    if diff == num :
        cnt -= 1 

print(cnt//2)
    