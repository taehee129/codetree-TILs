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


for _ in range(q) :
    a,b,c,d = map(int,input().split())

    a = linked[a-1]
    b = linked[b-1]
    c = linked[c-1]
    d = linked[d-1]

    prev_a = a.prev 
    next_b = b.next 
    prev_c = c.prev
    next_d = d.next
    
    if prev_a is not None :
        prev_a.next = c
    c.prev = prev_a
    if next_b is not None :
        next_b.prev = d 
    d.next = next_b

    if prev_c is not None : 
        prev_c.next =a 
    a.prev = prev_c
    if next_d is not None :
        next_d.prev = b 
    b.next = next_d
    for node in linked :
        print(node.prev.data if node.prev is not None else None, node.data , node.next.data if node.next is not None else None)
        # if node.prev is None :
        #     head = node
    print('*'*50)

