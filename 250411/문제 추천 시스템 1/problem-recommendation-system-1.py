from sortedcontainers import SortedSet 

s = SortedSet()

n = int(input())

for _ in range(n) : 
    (x,y) = tuple(map(int,input().split()))
    s.add((y,x))

m = int(input())

for _ in range(m) : 
    command = input()

    if command.startswith('rc') : 
        x= int(command.split()[1])

        if x == 1 :
            print(s[-1][1])
        else : 
            print(s[0][1])
    elif command.startswith('ad') : 
        x,y = map(int,tuple(command.split()[1:]))
        s.add((y,x))
    elif command.startswith('sv') : 
        x,y = map(int,tuple(command.split()[1:]))
        s.remove((y,x))
        


