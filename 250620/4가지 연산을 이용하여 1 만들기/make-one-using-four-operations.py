n = int(input())

def op(num, op) : 
    if op == 0 :
        return num-1 
    elif op == 1 :
        return num+1
    elif op == 2 : 
        return num/2 
    else : 
        return num/3

q= [] 
q.append((n,1))

ans = n
while q  :
    num,cnt = q.pop()
    
    for i in range(4) :
        if i==2 and num%2 != 0 :
            continue 
        if i==3 and num%3 != 0 :
            continue
        
        ret = op(num,i)
        if ret ==1 :
            ans = cnt 
            break
        
        q.insert(0,(ret,cnt+1))
        
    if ret ==1 :
            break

print(ans)

    

    