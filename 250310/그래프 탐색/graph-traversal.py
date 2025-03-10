n,m = tuple(map(int,input().split()))

matrix = [[0 for _ in range(n)] for _ in range(n)] 

for _ in range(m) : 
    x,y = tuple(map(int,input().split()))
    matrix[x-1][y-1] = 1 
    matrix[y-1][x-1] = 1

visited = [0 for _ in range(n)]


def dfs(vertex) :
    global n
    for i in range(n) :
        if matrix[vertex][i] == 1 and visited[i] ==0:
            visited[i] = 1
            dfs(i)

visited[0] = 1 
dfs(0)
print(visited.count(1)-1)

        