from sortedcontainers import SortedSet 

s = SortedSet([0])
n = int(input())
nums = list(map(int,input().split()))
import sys

MAX_SIZE=  sys.maxsize 

ans = MAX_SIZE

for num in nums:
    
    right = s.bisect(num)
    left = right-1
    ans = min((num- s[left]),ans)

    if right < len(s) : 
        ans = min(s[right] - num,ans)
    
    print(ans)

    s.add(num)
