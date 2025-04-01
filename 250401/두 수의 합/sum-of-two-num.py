n,k = map(int,input().split())


nums = list(map(int,input().split()))

d = {}

for num in nums :
    if num not in d :
        d[num]=True
    
nums = list(d.keys())

cnt =0
for i in range(n) :
    for j in range(i+1,n) :
        if nums[i] +nums[j] == k :
            cnt +=1


print(cnt)
