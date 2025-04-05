from sortedcontainers import SortedDict 

sd = SortedDict()

def order(string) : 
    
    if string.startswith('add') : 
    
        key,value = map(int, string.split()[1:])
        sd[key] = value 
    elif string.startswith('remove') : 
        key = int(string.split()[1])
        if key in sd :
            sd.pop(key)
    elif string.startswith('find') :
        key = int(string.split()[1])
        if key in sd :
            print(sd[key])
        else :
            print('None')
    else : 
        if len(sd.items()) == 0 :
            print('None')
            return 
        
        for item in sd.items() :
            print(item[1], end=' ')
        print()

n= int(input())

for _ in range(n) :
    order(input())
