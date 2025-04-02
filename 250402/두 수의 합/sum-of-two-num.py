n,k = map(int,input().split())


nums = list(map(int,input().split()))

d = [0 for _ in range(n)]
num_dict = {}

for i in range(n) : 
    num = nums[i]
    if (k-num) in num_dict : 
        d[i] = num_dict[k-num]

    if num in num_dict :
        num_dict[num] +=1 
    else : 
        num_dict[num] =1
     

cnt = 0 

for v in d :
    cnt +=v

print(cnt)
    