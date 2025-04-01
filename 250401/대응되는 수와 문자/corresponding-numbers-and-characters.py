n,m = map(int,input().split())

d= {}
d2 = {}
for i in range(n) :
    s = input()
    d[s] = i+1
    d2[i+1] = s

for _ in range(m) : 
    s = input()
    if s.isdigit() :
        print(d2[int(s)])
    else : 
        print(d[s])