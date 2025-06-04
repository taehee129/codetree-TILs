class Node :
    def __init__(self, data) :
        self.data =data
        self.prev = None 
        self.next = None 

def connect(node1,node2) :
    if node1 is not None :
        node1.next = node2 
    
    if node2 is not None :
        node2.prev = node1

def print_node(node) :
    if node is not None :
        return node.data 
    else : 
        return '-1'

n,q = map(int,input().split())

cities = list(map(lambda x:Node(x), input().split()))
pin = cities[0]

for i in range(n-1) :
    connect(cities[i],cities[i+1])
if n-1 != 0 :
    connect(cities[n-1],cities[0])

for _ in range(q) : 
    input_str = input()

    num = int(input_str[0])

    if num == 1 : 
        
        if pin.next is not None :
            pin = pin.next 
    
    if num == 2 :

        if pin.prev is not None :
            pin = pin.prev 


    if num == 3 : 

        node = pin.next

        if node is not None : 
            connect(node.prev, node.next)
    
    if num == 4 : 
        city = input_str.split()[1]
        node = Node(city)

        if pin.next is None : 
            connect(pin,node)
        else : 
            connect(node,pin.next)
            connect(pin,node)
    
    if pin.prev is None :
        print(-1)
    elif pin.prev.data == pin.next.data :
        print(-1)
    else : 
        print(pin.prev.data + ' ' + pin.next.data)    
            


