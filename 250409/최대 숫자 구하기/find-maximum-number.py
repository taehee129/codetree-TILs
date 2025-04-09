from sortedcontainers import SortedSet
n,m = tuple(map(int,input().split()))

nums = [i+1 for i in range(m)]

del_nums = list(map(int,input().split()))

s = SortedSet(nums)

for num in del_nums : 
    s.remove(num) 
    print(s[-1])
 