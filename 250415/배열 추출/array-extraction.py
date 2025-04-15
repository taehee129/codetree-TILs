n = int(input())

hq= []

import heapq as h

for _ in range(n) :
    num = int(input())

    if num == 0 :
        if hq :
            print(-h.heappop(hq))
        else :
            print(0)
    else :
        h.heappush(hq,-num)
    