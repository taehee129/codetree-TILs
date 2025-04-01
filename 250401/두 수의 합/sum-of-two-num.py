n,k = map(int,input().split())


nums = list(map(int,input().split()))

d = {}

for num in nums :
    if num not in d :
        d[num]=True
    
nums = list(d.keys())
end = len(nums)
cnt =0
for i in range(end) :
    for j in range(i+1,end) :
        if nums[i] +nums[j] == k :
            cnt +=1


print(cnt)
