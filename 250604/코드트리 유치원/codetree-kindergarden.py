class Node : 
    def __init__(self,data)  :
        self.data = data
        self.prev = None 
        self.next =None 

def connect(node1,node2) :
    if node1 is not None :
        node1.next =node2 
    if node2 is not None :
        node2.prev = node1 

q = int(input())

students = []

students.append(Node(1))
cnt=1
for _ in range(q) : 
    input_str=  input()
    num = int(input_str[0])

    if num == 1 :
        _,a,b = input_str.split()
        a = int(a)
        b = int(b)

        a_node = students[a-1]

        new_nodes = []

        for _ in range(b) : 
            cnt+=1
            new_nodes.append(Node(cnt))
        
        for i in range(b-1) :
            connect(new_nodes[i],new_nodes[i+1])
        
        students += new_nodes 

        connect(new_nodes[b-1],a_node.next)
        connect(a_node,new_nodes[0])
    
    elif num == 2 : 
        _,a,b = input_str.split()
        a = int(a)
        b = int(b)

        a_node = students[a-1]

        new_nodes = []

        for _ in range(b) : 
            cnt+=1
            new_nodes.append(Node(cnt))
        
        for i in range(b-1) :
            connect(new_nodes[i],new_nodes[i+1])
        
        students += new_nodes 

        connect(a_node.prev,new_nodes[0])
        connect(new_nodes[b-1],a_node)     
    else : 
        _,a = input_str.split()
        a = int(a)
        a = students[a-1]

        if a.prev is None or a.next is None :
            print(-1)
        else : 
            print(str(a.prev.data) + ' ' + str(a.next.data))


        



        

    

