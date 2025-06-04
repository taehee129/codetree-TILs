class Node :
    def __init__(self,data) :
        self.data = data
        self.prev = None 
        self.next=  None 

def connect(node1,node2) :
    if node1 is not None :
        node1.next =node2 
    if node2 is not None :
        node2.prev = node1 
n,m = map(int,input().split())

nums = list(map(lambda x:Node(int(x)),input().split()))

for i in range(n-1) :
    connect(nums[i],nums[i+1])

if n-1 != 0 :
    connect(nums[n-1],nums[0])

knights = dict()

for i in range(n) :
    knights[nums[i].data] = nums[i]



for _ in range(m) :
    called = int(input())

    node = knights[called]

    print(str(node.next.data)+' '+ str(node.prev.data))

    connect(node.prev,node.next)
    
    


