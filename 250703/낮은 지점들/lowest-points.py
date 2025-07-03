n= int(input())

positions = [map(int,input().split()) for _ in range(n)]

d = {}

for (x,y) in positions : 
    if x in d : 
        if y < d[x] :
            d[x] =y 
    else : 
        d[x] =y 

y_sum= 0
for x,y in d.items() : 
    y_sum +=y 

print(y_sum)