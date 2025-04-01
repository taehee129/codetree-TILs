n = int(input())

d = {}

def hashmap(order,k,v='') : 
    if order == 'add' : 
        d[k] = v
    elif order == 'remove' : 
        d.pop(k)
    else : 
        if k in d :
            print(d[k])
        else : 
            print('None')


for i in range(n) : 
    order, k,v = '','',''
    
    input_lst = input().split()

    if len(input_lst) == 3 :
        order,k,v = tuple(input_lst)
    else : 
        order, k = tuple(input_lst)
    
    hashmap(order,k,v)