from sortedcontainers import SortedSet

n,m = map(int,input().split())

want = list(map(int,input().split()))

chairs = SortedSet([i+1 for i in range(n)])

cnt = 0
for i in want : 
    idx = chairs.bisect_right(i)-1    
    if idx < 0 :    
        break
    chairs.remove(chairs[idx])
    cnt+=1
   
print(cnt)