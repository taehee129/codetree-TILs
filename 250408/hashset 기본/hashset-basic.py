n = int(input())

hs = set()
def order(input_str) : 
    if input_str.startswith('add') : 
        hs.add(input_str.split()[1])
    elif input_str.startswith('find') :
        if input_str.split()[1] in hs :
            print('true')
        else :
            print('false')
    else : 
        hs.remove(input_str.split()[1])

    
for _ in range(n) :
    order(input())