n = int(input())

nums = list(map(int,input().split()))
import sys 

min_dis = sys.maxsize
from sortedcontainers import SortedSet 

s = SortedSet() 
s.add(0)

for num in nums : 
    idx = s.bisect_right(num)

        
    if idx != len(s) :
        min_dis = min(min_dis, s[idx]-num)
    
    min_dis = min(min_dis,abs(s[idx-1]-num))
    print(min_dis)
    s.add(num)




