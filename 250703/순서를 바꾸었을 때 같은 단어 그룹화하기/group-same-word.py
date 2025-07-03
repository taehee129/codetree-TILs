n= int(input())

strs = [list(input()) for _ in range(n)]

d = {}

for s in strs : 
    s.sort()
    
    s = ''.join(s)

    if s in d :
        d[s] +=1 
    else : 
        d[s] = 1 


max_cnt = 0
max_str= ''
for k,v in d.items() :
    if max_cnt < v : 
        max_cnt = v 
        max_str = k

print(max_cnt)