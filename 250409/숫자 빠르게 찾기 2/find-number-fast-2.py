from sortedcontainers import SortedSet
n,m = map(int,input().split())

nums = list(map(int,input().split()))

s = SortedSet(nums)


for _ in range(m) : 
    num = int(input())
    ret = s.bisect_left(num) 

    if ret == len(s) :
        print(-1)
    else :
        print(s[ret])
    



