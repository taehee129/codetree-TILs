n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]

selected = []

rows_visited = [False]*n 

max_val = 0

def permutation(col) : 
    global max_val
    if col == n : 
        val = 0
        for x,y in selected :
            val+= grid[x][y]
            max_val = max(max_val,val)

        return
  
    for i in range(n) :
        if rows_visited[i] :
            continue 
        
        selected.append((i,col))
        rows_visited[i] = True 

        permutation(col+1)

        selected.pop()
        rows_visited[i] = False


permutation(0)
print(max_val)