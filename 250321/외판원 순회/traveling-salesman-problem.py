n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]

nums = [i for i in range(1,n)] 

visited = [False]*(n-1)

select= []

import sys

ans = sys.maxsize

def permuation() :
    global ans
    if len(select) == n-1 : 
       
        val = grid[0][select[0]]
    
        for i in range(len(select)) :
            if i == len(select)-1 : 
                val += grid[select[i]][0] 
                
                break
            val += grid[select[i]][select[i+1]]
          
        ans = min(ans,val)
        return

    for i in range(n-1) :
        if visited[i] :
            continue
        
        select.append(nums[i])
        visited[i] = True 

        permuation()

        select.pop()
        visited[i] = False

permuation()
print(ans)


