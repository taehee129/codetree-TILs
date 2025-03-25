n = int(input())


def op(num,op) : 

    if  op == 0 : 
        return num-1
    elif op == 1 :
        return num+1
    elif op ==2 :
        return num/2 
    elif op ==3 :
        return num/3


def bfs(num) :

    q = [(num,0)]

    while len(q) >= 1 :

        num,idx = q.pop()
        if num ==1 :
            return idx

        for i in range(4) :
            if i == 2 and num %2 !=0 :
                continue 
            if i ==3 and num %3 != 0 :
                continue 
            
            q.insert(0,(op(num,i),idx+1))
        

print(bfs(n))
            


            

        



    
