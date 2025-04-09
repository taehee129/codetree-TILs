from sortedcontainers import SortedSet

t = int(input())

s = SortedSet()
for _ in range(t) : 
    k = int(input())
    for _ in range(k) :
        c,n = tuple(input().split())
        n= int(n)

        if c == 'I' : 
            s.add(n) 
        else : 
            if n ==1 :
                if  s :
                    s.remove(s[-1])
            else :
                if s :
                    s.remove(s[0])
        
    if len(s) >=1: 
        print(s[-1], s[0])
    else :
        print('EMPTY')



