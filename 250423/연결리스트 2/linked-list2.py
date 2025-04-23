class Node :
    def __init__(self,data) :
        self.data =data
        self.prev= None
        self.next =None 
    

def insert_next(a,b ) : 
    b.next = a.next
    b.prev = a

    if a.next is not None :
        a.next.prev = b
    
    a.next = b

def insert_prev(a,b) :
  
    b.next= a 
    b.prev = a.prev
    
    if a.prev is not None :
        a.prev.next =b 
    a.prev = b

  


def pop(a) :
    if a.next is not None: 
        a.next.prev = a.prev 
    
    if a.prev is not None :
        a.prev.next = a.next 
    
    a.next = None 
    a.prev = None 


n = int(input())
q = int(input())

linked = [None]*n

for i in range(n) :
    linked[i] = Node(i)

for _ in range(q) :
    arr = input().split()
    order = int(arr[0])

    if order == 1 :
        i = int(arr[1])
        if linked[i-1] is not None :
            pop(linked[i-1])

    elif order == 2 :
        i,j = int(arr[1]),int(arr[2])
        insert_prev(linked[i-1],linked[j-1])
    
    elif order ==3  :
        i,j = int(arr[1]),int(arr[2])
        insert_next(linked[i-1],linked[j-1])

    elif order == 4:
        i = int(arr[1])
        node = linked[i-1]

        if node.prev is not None :
            print(node.prev.data+1, end=' ')
        else :
            print(0, end =' ')
        
        if node.next is not None :
            print(node.next.data+1)
        else :
            print(0)

for i in range(n) :
    print(linked[i].next.data+1 if linked[i].next is not None else 0 , end = ' ') 