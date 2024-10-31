# 사다리 타는 함수 
# 경우의 수를 만드는 함


n,m = tuple(map(int, input().split()))

maxM= 15

line= list()

origin = [
    [False]*n
    for _ in range(maxM)
]


for i in range(m) :
    
    x,y = tuple(map(int,input().split()))
    line.append((y,x))
    origin[y-1][x-1] = True


def doLadder(y,lst) : 
    global n
    for i in range(15) :
        
        if y-1>=0 and lst[i][y-1]== True:
            y= y-1
        elif y+1<n and lst[i][y] == True :
            y= y+1

    return y


def makeLadder(line, permuList) :
    global maxM
    global n
    lst =[
        [False]*n
        for _ in range(maxM)
    ]

    for i,(x,y) in enumerate(line) :
        lst[x-1][y-1] = permuList[i]
    return lst

asw =15
permuList =[]
def permutation2(a) :
    global asw
    permuList.append(flag)
    if len(permuList) == len(line) :

        check= False
        lst =makeLadder(line,permuList)
        
        for i in range(4) :
            if doLadder(i,lst) == doLadder(i,origin) :
                check =True
        if check :
            asw = min(asw,permuList.count(True))

        return
    


def permutation(lst) : 
    if len(lst) == len(line) :
        permuList.append(lst)
        return
    
    lst1 = lst[:]
    lst1.append(True)
    permutation(lst1)

    lst2 = lst[:]
    lst2.append(False)
    permutation(lst2)


permutation([])

for i,per in enumerate(permuList) :
    
    check= True
    lst =makeLadder(line,per)
    
    for i in range(n) :
        if doLadder(i,lst) != doLadder(i,origin) :
            check =False
    if check :
        asw = min(asw,per.count(True))

print(asw)