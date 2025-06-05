class Node : 
    def __init__(self,data) : 
        self.data = data
        self.prev = None 
        self.next = None 

def connect(n1,n2) : 
    if n1 is not None :
        n1.next = n2 
    if n2 is not None :
        n2.prev= n1
n,m,q = map(int,input().split())

students = dict()

for _ in range(m) : 
    lst = list(map(int,input().split()))
    cnt = lst[0]
    lst = lst[1:]

    for i in range(cnt) : 
        data = lst[i]
        node = Node(data-1)
        students[data-1] = node 
        if i != 0 : 
            connect(students[lst[i-1]-1],students[lst[i]-1])

    connect(students[lst[cnt-1]-1],students[lst[0]-1])    

# for _ in range(m) : 
#     lst = list(map(int,input().split()))
#     cnt = lst[0]
#     lst = lst[1:]

#     for i in range(cnt-1) : 
#         connect(students[lst[i]-1],students[lst[i+1]-1])
    
#     connect(students[lst[cnt-1]-1],students[lst[0]-1])

# node = students[1]

for _ in range(q) : 
    input_lst= input().split()

    flag = int(input_lst[0])

    if flag == 1 : 
        _,a,b = map(int,input_lst)

        a,b = students[a-1], students[b-1] 

        
        if a.next is not None : 
            a.next.prev  = b.prev
        if b.prev is not None : 
            b.prev.next = a.next
        a.next = b 
        b.prev = a 

    elif flag == 2 :
        _,a,b = map(int,input_lst)
        a,b = students[a-1], students[b-1] 
        
        after_a_prev = b.prev 
        if a.prev is not None : 
            a.prev.next= b 
        b.prev = a.prev 
        a.prev = after_a_prev
        if after_a_prev is not None : 
            after_a_prev.next = a
            
    elif flag == 3 : 
        _,a = map(int,input_lst)

        a = students[a-1]
        node = a 
        min_node = 1000000 
     
        while True :
            min_node = min(min_node,node.data)
           
            node= node.next           
            if node.data == a.data : 
                break 
        
        node = students[min_node]
        while True :
            print(node.data+1, end = ' ')
            node = node.prev 
            if node.data == min_node : 
                break 






