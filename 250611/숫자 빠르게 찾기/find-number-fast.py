num_dict = dict()

n,m = map(int,input().split())

nums = list(map(int,input().split()))

for i in range(n) : 
    num_dict[nums[i]] = i+1 


for _ in range(m) : 
    num = int(input())
    
    if num in num_dict : 
        print(num_dict[num])
    else :
        print(-1)
