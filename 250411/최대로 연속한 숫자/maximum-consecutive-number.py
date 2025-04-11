n,m = map(int,input().split())
nums = list(map(int,input().split()))
from sortedcontainers import SortedSet 

s = SortedSet()

s.add((0,n))

for num in nums :
    idx = s.bisect_right((num,0))
    a,b = s[idx-1]

    s.remove((a,b))
    if a <= num-1 :
        s.add((a,num-1))
    if b>= num+1 :
        s.add((num+1,b))

    max_len = 0
    for x,y in s : 
        max_len= max(max_len, y-x+1)

    print(max_len)