from sortedcontainers import SortedSet

n,m = map(int,input().split())

nums = list(map(int,input().split()))
ss = SortedSet(nums)
for _ in range(m) :
    num = int(input())

    ans = ss.bisect_left(num)

    if ans == len(ss) : 
        print(-1)
    else :
        print(ss[ans])