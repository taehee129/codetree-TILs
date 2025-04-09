from sortedcontainers import SortedSet 
n,m = map(int,input().split())


s = SortedSet()

for _ in range(n) : 
    s.add(tuple(map(int,input().split())))

for _ in range(m) : 
    
    ret = s.bisect_right(tuple(map(int,input().split())))

    if ret == n:
        print(-1,-1)
    else :
        print(s[ret][0],s[ret][1])