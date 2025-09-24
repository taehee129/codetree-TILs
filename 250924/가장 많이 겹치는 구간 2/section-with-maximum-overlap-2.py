n = int(input())

segments = [tuple(map(int,input().split())) for _ in range(n)]

points =[] 


for x1,x2 in segments : 
    points.append((x1,1))
    points.append((x2,-1))


points.sort()

ans = 0
sumVal = 0
for x , v in points:
    sumVal +=v 

    ans = max(ans,sumVal)

print(ans)
    