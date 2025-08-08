from sortedcontainers import SortedSet

t = int(input())

for _ in range(t) :
    k = int(input())

    ss = SortedSet()

    for _ in range(k) : 
        oper, n= tuple(input().split())
        n = int(n)

        if oper == 'I' : 
            ss.add(n)
        else : 
            if len(ss) == 0 :
                continue 
            
            if n == 1 : 
                del ss[-1]
            else :
                del ss[0]


    if len(ss) != 0 : 
        print(ss[-1],ss[0])       
    else : 
        print('EMPTY')     
