from sortedcontainers import SortedSet
 
n,m = map(int,input().split())


coordinate = [tuple(map(int,input().split())) for _ in range(n)]

s = SortedSet(coordinate)


for _ in range(m) : 
    num = int(input())
    idx = s.bisect_left((num,0))

    if idx == len(s) : 
        print(-1,-1)
        continue

    print(s[idx][0], s[idx][1])
    s.remove(s[idx])
    
