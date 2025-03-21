n = int(input())

# Please write your code here.

nums = [i for i in range(1,n+1)]
answer =[]
visited = [False]*n

def choose(idx) : 
    if idx == n : 
        print(' '.join(map(str,answer)))
    
    for i in range(n-1,-1,-1) :
        if visited[i] :
            continue 

        answer.append(nums[i])
        visited[i] = True 

        choose(idx+1)

        answer.pop()
        visited[i] = False 

choose(0) 
