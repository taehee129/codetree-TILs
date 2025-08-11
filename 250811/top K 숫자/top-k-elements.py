n,k = map(int,input().split())

nums = list(map(int,input().split()))

from sortedcontainers import SortedSet 

s = SortedSet(nums)

for i in range(k) : 
    print(s[-(1+i)],end=' ')
