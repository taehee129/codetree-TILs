n,k = map(int,input().split())

set_lst = [{i} for i in range(n)] 
lst = [i for i in range(n)]

def swap(a,b) : 
    lst[a],lst[b] = lst[b], lst[a]
    set_lst[lst[a]].add(b)
    set_lst[lst[b]].add(a)


swap_lst = [tuple(map(int,input().split())) for _ in range(k)]

for i in range(3*k) : 
    a, b = swap_lst[i%k]
    swap(a-1,b-1)
    

for s in set_lst : 
    print(len(s))




 