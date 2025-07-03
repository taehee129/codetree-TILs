n= int(input())



sequences= [list(map(int,input().split())) for _ in range(4)]


d1 = {}
d2 = {}
for i in range(n) :
    for j in range(n) :
        s = sequences[0][i] + sequences[1][j] 
        if s in d1 : 
            d1[s] +=1 
        else : 
            d1[s] =1 
    
for i in range(n) :
    for j in range(n) :
        s = sequences[2][i] + sequences[3][j] 
        if s in d2 : 
            d2[s] +=1 
        else : 
            d2[s] =1 

cnt =0

for k,v in d1.items() : 
    if -k in d2 : 
        cnt += d2[-k]*v 

print(cnt)
        