n= int(input())

d = {}


for _ in range(n) :
    string = input()
    if string in d :
        d[string] +=1 
    else :
        d[string] = 1 
    

max_cnt = 0 

for val in d.values() :
    max_cnt = max(max_cnt, val)

print(max_cnt)