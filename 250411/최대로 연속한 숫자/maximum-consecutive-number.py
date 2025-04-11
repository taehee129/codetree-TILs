n,m = map(int,input().split())
nums = list(map(int,input().split()))
from sortedcontainers import SortedSet 

s = SortedSet()

s.add((0,n))

sum_set = SortedSet()
sum_set.add((n-0+1,0,n))
for num in nums :

    idx = s.bisect_right((num,0))
    a,b = s[idx-1]
    
    s.remove((a,b))
    sum_set.remove((b-a+1,a,b))
    if a <= num-1 :
        s.add((a,num-1))
        sum_set.add((num-1-a+1,a,num-1))
    if b>= num+1 :
        s.add((num+1,b))
        sum_set.add((b-num-1+1,num+1,b))
    
    
    print(sum_set[-1][0])
    
    
