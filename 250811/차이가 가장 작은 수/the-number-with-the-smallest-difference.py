n,m = map(int,input().split())

nums = []

for _ in range(n) : 
    nums.append(int(input())) 

from sortedcontainers import SortedSet 

s = SortedSet(nums)

import sys

ans = sys.maxsize

for i in s : 
    idx1=s.bisect_left(i+m)
    idx2=s.bisect_right(i-m)-1
    
    #print(i, idx1,idx2)
    if idx1 != len(s) : 
        ans = min( s[idx1] - i ,ans)
    
    if idx2 >=0 :
        ans = min(i-s[idx2],ans)

if ans == sys.maxsize : 
    print(-1)
else : 

    print(ans)