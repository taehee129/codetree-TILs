# 이중 연결 리스트 

class Node : 
    def __init__(self, data) : 
        self.data = data
        self.prev = None
        self.next = None


def insert_next(node,singleton) : 
    singleton.next = node.next 
    singleton.prev = node

    if singleton.next is not None :
        singleton.next.prev = singleton
    if singleton.prev is not None :
        singleton.prev.next = singleton

    

def insert_prev(node,singleton) : 
    singleton.next =node 
    singleton.prev = node.prev

    if singleton.next is not None :
        singleton.next.prev = singleton 
    
    if singleton.prev is not None :
        singleton.prev.next= singleton 
    
def pop(u) :
    if u.next is not None :
        u.next.prev = u.prev
    if u.prev is not None :
        u.prev.next = u.next
    u.prev = u.next= None


def swap(a,b) : 

    tempa = a
    tempb = b 

    a.next = b.next 
    a.prev = b

    b.next= a
    b.prev = tempa.prev 


cur = Node(input())

n = int(input())

for _ in range(n) :
    s = input()

    if s.startswith('1') :
        word = s.split()[1] 
        node = Node(word)
        insert_prev(cur,node)
    
    elif s.startswith('2') : 
        word = s.split()[1] 
        node = Node(word)
        insert_next(cur,node)      
    
    elif s.startswith('3') :
        if cur.prev is not None : 
            cur = cur.prev

            
    elif s.startswith('4') :
        if cur.next is not None :
            cur = cur.next

    if cur.prev is not None : 
        print(cur.prev.data, end =' ')
    else :
        print('(Null)', end =' ')
    
    if cur is not None : 
        print(cur.data, end =' ')
    else :
        print('(Null)', end = ' ')

    if cur.next is not None : 
        print(cur.next.data)
    else :
        print('(Null)')
     


        
