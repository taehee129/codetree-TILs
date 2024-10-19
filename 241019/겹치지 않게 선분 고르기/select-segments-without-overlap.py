n = int(input())


line =[
    list(map(int,input().split()))
    for _ in range(n)
]
answer=0

def check(lst, obj) :
    for i in lst :
        if (line[i][0] <= obj[0] and line[i][1] >= obj[0]) or (line[i][0] <= obj[1] and line[i][1] >= obj[1]) :
            return False
    return True
    


def choose(index, lst) :
    global answer

    lst = list(lst)
    if index== n : 
        answer = max(answer,len(lst))

        return

    for i in range(index,n) :
      
        if check(lst,line[i]) :
            lst.append(i)

        choose(i+1,lst)

        


 


choose(0,[])
print(answer)