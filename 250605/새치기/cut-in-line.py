class Node :
    def __init__(self,data) :
        self.data = data
        self.prev = None 
        self.next = None 
        self.head = None 

def connect(a,b) :
    if a is not None :
        a.next = b 
    if b is not None :
        b.prev = a 

n,m,q = map(int,input().split())


people = [Node(i) for i in range(n)]

lines = [] 

def chage_head(a,b) : 
    line  = a.head 
    a.head = None 
    b.head = line 
    lines[line] = b

for k in range(m) : 
    lst = list(map(int,input().split()))

    if lst[0] == -1 : 
        lines.append(None)
        continue
    
    cnt = lst[0]
    lst = lst[1:]

    for i in range(cnt-1) :
        a,b = people[lst[i]-1], people[lst[i+1]-1]
        connect(a,b)

    people[lst[0]-1].head = k
    lines.append(people[lst[0]-1])



for _ in range(q) : 
    input_str = input()
    num = int(input_str.split()[0])

    if num == 1 : 
        _,a,b = map(int,input_str.split())

        a,b = people[a-1],people[b-1]
        
        if a.head is not None : 
            if a.next is None : 
                line = a.head 
                lines[line] = None
            else : 
                chage_head(a,b)
    
        connect(a.prev,a.next)
    
        connect(b.prev,a)
        connect(a,b)

        if b.head is not None : 
            chage_head(b,a)

    elif num ==2  :
        _,a  = map(int,input_str.split())
        a = people[a-1]
        connect(a.prev,a.next)
        
        if a.head is not None : 
            line = a.head 
            if a.next is None : 
                lines[line] = None
            else : 
                chage_head(a,b)

    elif num == 3 : 
        _,a,b,c = map(int,input_str.split())
        a,b,c = people[a-1],people[b-1],people[c-1]
        connect(a.prev,b.next)

        if a.head is not None : 
            if b.next is None : 
                line = a.head 
                lines[line]= None 
            else : 
                chage_head(a,b.next)

        connect(c.prev,a)
        connect(b,c)

        if c.head is not None : 
            chage_head(c,a)


for i in range(m) :   
    node = lines[i]

    if node is None :
        print(-1)
        continue
    
    while True : 
        if isinstance(node, int) : 
            print('int : '+ str(node))
            break
        else :
            print(node.data+1, end = ' ')
        node = node.next
        if node is None :
            break
        
    print()