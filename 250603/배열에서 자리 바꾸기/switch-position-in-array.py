class Node :
    def __init__(self,data) :
        self.data = data
        self.prev= None 
        self.next = None 
    


n = int(input())
q = int(input())

lst = [Node(i+1) for i in range(n)]

for i in range(n) :
    if i >=1 :
        lst[i].prev = lst[i-1]
    if i != n-1:
        lst[i].next = lst[i+1]

    
for _ in range(q) : 
    a,b,c,d = map(int,input().split())

    a_node= lst[a-1]
    b_node = lst[b-1]
    c_node = lst[c-1]
    d_node = lst[d-1]

    a_node_prev = a_node.prev 
    b_node_next = b_node.next
    c_node_prev = c_node.prev 
    d_node_next = d_node.next
    
    if c_node_prev is not None and c_node_prev.data == b_node.data :
        c_node_prev = d_node
    a_node.prev = c_node_prev
    if c_node_prev is not None :
        c_node_prev.next= a_node
    if d_node_next is not None and d_node_next.data == a_node.data :
        d_node_next = c_node
    b_node.next = d_node_next
    if d_node_next is not None :
        d_node_next.prev = b_node
    
    if a_node_prev is not None and a_node_prev.data ==d_node.data :
        a_node_prev = b_node 
    c_node.prev = a_node_prev
    if a_node_prev is not None :
        a_node_prev.next =c_node
    if b_node_next is not None and b_node_next.data ==  c_node.data :
        b_node_next = a_node
    d_node.next = b_node_next
    if b_node_next is not None :
        b_node_next.prev = d_node


for i in range(n) :
    if lst[i].prev is None :
        first = lst[i]
        break 

node = first
while True : 
    print(node.data, end = ' ')
    if node.next is not None :
        node = node.next 
    else :
        break 

    
