n= int(input())
grid = [list(map(int,input().split())) for _ in range(n)]


selected = []

rows = [False]*n
cols = [False]*n 

max_val = 0

def permutation() :
    global max_val
    if len(selected) == n :
        val = 0 
        for x,y in selected :
            val += grid[x][y]

        max_val = max(max_val,val)
    
        return 
    
    for i in range(n) :
        for j in range(n) : 
            if rows[i] or cols[j] :                
                continue 
            
            selected.append((i,j))
            rows[i] = True
            cols[j] = True 

            permutation()

            selected.pop()
            rows[i] = False
            cols[j] = False

permutation()
print(max_val)

