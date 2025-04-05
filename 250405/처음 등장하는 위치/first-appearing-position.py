n = int(input())

nums = list(map(int,input().split()))

from sortedcontainers import SortedDict 

sd = SortedDict()

for i in range(n) :
    num = nums[i]

    if num in sd :
        continue 
    
    sd[num] = i+1


for k,v in sd.items() :
    print(k,v)

