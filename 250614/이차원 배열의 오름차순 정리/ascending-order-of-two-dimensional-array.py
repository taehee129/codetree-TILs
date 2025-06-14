n= int(input())
k= int(input())

matrix = [[(i+1)*(j+1) for j in range(n)] for i in range(n)]


grid = [0]*((n+1)**2)

for i in range(n) :
    for j in range(n) :
        val = matrix[i][j]
        grid[val] +=1 


cnt = 0
for i in range((n+1)**2) :
    cnt += grid[i]
    if cnt >= k :
        break 

print(i)