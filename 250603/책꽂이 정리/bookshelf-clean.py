
class Node  :
    def __init__(self,data) :
        self.data = data
        self.prev = None
        self.next = None

def connect(a,b) : 
    if a is not None :
        a.next = b
    if b is not None :
        b.prev = a

n,k= map(int,input().split())
q = int(input())

shelves = [[None,None] for _ in range(k)]

books = [Node(i) for i in range(n)] 

for i in range(n-1) : 
    connect(books[i],books[i+1])

shelves[0][0] = books[0]
shelves[0][1] = books[n-1]
for _ in range(q) : 
    num,i,j = map(int,input().split())
    i = i-1
    j -=1
    if num == 1 : 
        if shelves[i][0] is None : 
            continue 
        
        book = shelves[i][0] 

        if book.next is not None : 
            shelves[i][0] = book.next
            shelves[i][0].prev = None 
        else : 
            shelves[i][0] = None
            shelves[i][1] = None
        book.prev = None 
        book.next = None


        if shelves[j][1] is not None :
            connect(shelves[j][1],book)
            shelves[j][1] = book
        else : 
            shelves[j][0] = shelves[j][1] = book
    elif num ==2 :
        if shelves[i][0] is None : 
            continue 
        
        head,tail = shelves[i][0], shelves[i][1]

        book = tail 
        
        if tail.prev is not None : 
            tail.prev.next = None
            tail = tail.prev
        else : 
            head = tail = None 
        book.prev = book.next = None 
        shelves[i][0], shelves[i][1] =  head,tail
        head,tail = shelves[j][0], shelves[j][1]
     
        if head is not None :
            connect(book,head)
            head = book
        else : 
            head = book 
            tail = book

        shelves[j][0],shelves[j][1] = head,tail

    elif num ==3 : 
        head,tail = shelves[i][0],shelves[i][1]
        if head is None :
            continue 
        
        head2,tail2 = shelves[j][0], shelves[j][1]

        if head2 is not None and head.data != head2.data : 
            connect(tail,head2)
            head2 = head
            head = tail = None
        else : 
            head2 = head 
            tail2 = tail 
            head = tail = None
            

        shelves[i][0] , shelves[i][1] = head,tail 
        shelves[j][0] , shelves[j][1] = head2,tail2
    elif num == 4 :
        head,tail = shelves[i][0],shelves[i][1]
        if head is None :
            continue 
        
        head2,tail2 = shelves[j][0], shelves[j][1]

        if head2 is not None and head.data != head2.data  : 
            connect(tail2,head)
            tail2 = tail 
            tail = head = None 
        else : 
            head2 = head 
            tail2 = tail 
            head = tail = None

        shelves[i][0] , shelves[i][1] = head,tail 
        shelves[j][0] , shelves[j][1] = head2,tail2




for i in range(k) :
    node = shelves[i][0]
    s = ''
    cnt =0 
    while True : 
        if node is None :
            break
        s+= str(node.data+1) + ' '
        cnt +=1 
        node = node.next
    
    print(str(cnt)+' '+s)





        

          
        
    
    