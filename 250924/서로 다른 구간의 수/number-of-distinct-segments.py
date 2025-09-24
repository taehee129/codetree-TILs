n= int(input())

segments = [tuple(map(int,input().split())) for _ in range(n)]

points = []

for i,(x1,x2) in enumerate(segments) :
    points.append((x1,1,i))
    points.append((x2,-1,i))

segs = set()

points.sort()

ans = 0

for x,v,i in points : 
    if v == 1 :
        if len(segs) ==0 : 
            ans +=1 
        segs.add(i)
    
    else : 
        segs.remove(i)

print(ans)