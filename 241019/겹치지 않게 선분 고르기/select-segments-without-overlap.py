n = int(input())


line =[
    list(map(int,input().split()))
    for _ in range(n)
]
answer=0


def check(lst, obj):
    for i in lst:
        # Check if there is any overlap between two intervals
        if not (line[i][1] < obj[0] or line[i][0] > obj[1]):
            return False
    return True

def choose(index, lst) :
    global answer
  
    if index== n : 
        
        answer = max(answer,len(lst))


        return

    for i in range(index,n) :
        flag = check(lst,line[i])
        if flag:
            lst.append(i)
        
        choose(i+1,lst)
        if flag :
            lst.pop()
        




choose(0,[])
print(answer)