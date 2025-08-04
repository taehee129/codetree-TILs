n,k = map(int,input().split())

chairs= [i for i in range(n)]
lst = [] 
for _ in range(k) : 
    lst.append(tuple(map(int,input().split())))

cnt_lst = [set([i]) for i in range(n)]

def change(x,y) : 
    chairs[x],chairs[y] = chairs[y], chairs[x] 

    a,b = chairs[x] ,chairs[y]

    if x not in cnt_lst[a] :
        cnt_lst[a].add(x)
    if y not in cnt_lst[b] :
        cnt_lst[b].add(y)

for i in range(3*k) :
    x,y = lst[i%k]
    change(x-1,y-1)

for s in cnt_lst : 
    print(len(s))