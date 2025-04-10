from sortedcontainers import SortedSet

n,k = map(int,input().split())

nums = SortedSet(map(int,input().split()))

for _ in range(k) :
    print(nums[-1], end = ' ')
    nums.remove(nums[-1]) 
    