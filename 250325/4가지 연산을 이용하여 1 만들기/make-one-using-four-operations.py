n = int(input())


def op(num,op) : 

    if  op == 0 : 
        return num-1
    elif op == 1 :
        return num+1
    elif op ==2 :
        return int(num/2) 
    elif op ==3 :
        return int(num/3)

visited = [False]*1000000

def bfs(num) :

    q = [(num,0)]
    visited[num-1] = True
    while len(q) >= 1 :

        num,idx = q.pop()
        #print(num,idx)
        if num ==1 :
            return idx

        for i in range(4) :
            
            if i == 2 and num %2 !=0 :
                continue 
            if i ==3 and num %3 != 0 :
                continue 
            
            new_num = op(num,i)
            
            if visited[new_num-1] : 
                continue

            q.insert(0,(new_num,idx+1))
            visited[new_num-1] = True
        

print(bfs(n))
            


            

        



    
