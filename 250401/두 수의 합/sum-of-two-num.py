n,k = map(int,input().split())


nums = list(map(int,input().split()))

cnt =0
for i in range(n) :
    for j in range(i,n) :
        if nums[i] +nums[j] == k :
            cnt +=1


print(cnt)
