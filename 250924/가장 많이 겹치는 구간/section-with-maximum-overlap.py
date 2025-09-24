n = int(input())

points = [tuple(map(int,input().split())) for _ in range(n)]


lst = []

for x1,x2 in points : 
    lst.append((x1,1))
    lst.append((x2,-1))


lst.sort()

maxVal = 0
ans = 0
sumVal = 0
for x, val in lst : 
    #print(x,val)
    sumVal += val 
    ans = max(ans,sumVal)

print(ans)

    

