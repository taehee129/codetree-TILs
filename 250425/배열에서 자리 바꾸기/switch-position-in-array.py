class Node :
    def __init__(self,data) :
        self.data =data
        self.prev = None 
        self.next = None 

n = int(input())
q = int(input())


linked = [] 

for i in range(n) : 
    node = Node(i+1)

    linked.append(node)

    if i !=0 : 
        prev_node = linked[i-1] 
        prev_node.next = node                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        node.prev = prev_node

def pop(node1,node2) : 
    if node1.prev is not None :
        node1.prev.next = node2.next 
    if node2.next is not None :
        node2.next.prev = node1.prev

def link(node1,node2) :
    node1.next = node2
    node2.prev = node1

def insert_prev(node1,node2) :
    link(node2,node1)
    if node1.prev is not None :
        link(node1.prev, node2)

def insert_next(node1,node2) : 
    link(node1,node2)
    if node1.next is not None :
        link(node2,node1.next)

def swap(a,b,c,d) : 
    c_prev = c.prev 
    d_next = d.next

    c.prev = a.prev
    if a.prev is not None :
        a.prev.next =c 
    
    d.next = a 
    a.prev = d
    b.next = d_next 
    if d_next is not None :
        d_next.prev = b

for _ in range(q) :
    a,b,c,d = map(int,input().split())

    a = linked[a-1]
    b = linked[b-1]
    c = linked[c-1]
    d = linked[d-1]

    if (b.next is not None and b.next.data == c.data)  :
        swap(a,b,c,d)
        
    elif (d.next is not None and d.next.data == a.data):
        swap(c,d,a,b)
    else : 
        a_prev = a.prev
        b.next = b.next
        c_prev = c.prev
        d_next = d.next 

        c.prev = a.prev 
        d.next = b.next 
        
        if a.prev is not None :
            a.prev.next = c
        if b.next is not None :
            b.next.prev = d

        a.prev = c_prev 
        b.next = d_next 

        if c_prev is not None :
            c_prev.next = a
        if d_next is not None :
            d_next.prev = b 

    # for node in linked :
    #     print(node.prev.data if node.prev is not None else None, node.data,node.next.data if node.next is not None else None)
    # print('*'*50)


for node in linked :
    if node.prev is None :
        head = node

node = head
for i in range(n) :
    print(node.data, end=' ')
    node = node.next
    


    
    

   

