from sortedcontainers import SortedSet

n = int(input())

s=  SortedSet()
for _ in range(n) : 

    command = input()

    if command.startswith('add') :
        
        s.add(int(command.split()[1]))
   
    elif command.startswith('remove') :
        s.remove(int(command.split()[1])) 
    
    elif command.startswith('find') : 

        if int(command.split()[1]) in s : 
            print('true')
        else :
            print('false')
    
    elif command.startswith('lower_bound') :       
        idx = s.bisect_left(int(command.split()[1]))
        if idx == len(s) :
            print('None')
        else :
            print(s[idx])
    elif command.startswith('upper_bound') :
        idx =s.bisect_right(int(command.split()[1]))
        if idx == len(s) :
            print('None')
        else :
            print(s[idx])
    elif command == 'largest' :
        if s :
            print(s[-1] )
        else :
            print('None')

    else :
        if s :
            print(s[0])
        else :
            print('None')