n= int(input())
q = int(input())

class Node : 
    def __init__(self,data) :
        self.data = data
        self.prev = None 
        self.next = None

lst = [Node(i+1) for i in range(n)]
def print_node(node) :
    return node.data if node is not None else 0


for _ in range(q) :
    input_str = input()
    num = int(input_str[0])

    if num ==1 :
        _, i = input_str.split()
        i = int(i)

        node = lst[i-1]
        
        if node.prev is not None :
            node.prev.next = node.next 
        if node.next is not None :
            node.next.prev = node.prev
        node.next = None 
        node.prev = None 
    if num == 2 :
        _,i,j = input_str.split()
        i = int(i)
        j = int(j)
        single = lst[j-1]

        node = lst[i-1]

        single.next = node 
        single.prev = node.prev 

        if single.next is not None :
            single.next.prev = single
        if single.prev is not None :
            single.prev.next = single 
        
    if num == 3: 
        _,i,j = input_str.split()
        i = int(i)
        j = int(j)
        single = lst[j-1]
        node = lst[i-1]

        single.prev = node 
        single.next =node.next 

        if single.prev is not None :
            single.prev.next = single 
        if single.next is not None :
            single.next.prev = single
    if num ==4 :
        _,i = input_str.split()
        i = int(i)
        node = lst[i-1]

        print(print_node(node.prev), print_node(node.next)) 

for i in range(n) :
    print(print_node(lst[i].next),end =' ')