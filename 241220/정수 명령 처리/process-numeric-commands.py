
lst =[]
def stack(s,num) :
    if s =="push" : 
        lst.append(num)
    elif s=="pop" :
        print(lst[-1])
        del lst[-1]
    elif s =="size" :
        print(len(lst))
    elif s=="empty" :
        print(int(len(lst)==0))
    elif s=="top" :
        print(lst[-1])

n = int(input())

for _ in range(n) :  
    a = input().split()
    if len(a) == 1 : 
        s,num = (a[0],_) 
    else :
        s,num = (a[0],a[1])
    #print(s,num)
    stack(s,num)
