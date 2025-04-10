n,m = map(int,input().split())

nums = []

for _ in range(n) :
    nums.append(int(input()))

from sortedcontainers import SortedSet 

s = SortedSet(nums)

import sys

min_diff  = sys.maxsize
for num in nums :
    num1 = num +m 

    ret= s.bisect_left(num1)

    if ret != n :
        min_diff = min(min_diff, s[ret]-num)
    
    
    num2 = num -m 

    if num2 >=1 :
        ret2 = s.bisect_right(num2)
        if ret2 != 0 :
            min_diff = min(min_diff, num-s[ret2-1])
    
print(min_diff)


    
    
