n= int(input())

matrix = [
    
    list(map(int, input().split()))
    for _ in range(n)
]


# x-2, x-1,x+1,x+2 
# x-1,y-1,x+1,y+1, (x+1,y+1),(x-1,y-1), (x+1,y-1),(x-1,y+1)
def validation(x,y) :
    if x >=0 and x < n and y>=0 and y<n :
        return True


def explode(x,y,k,lst) :
    lst[x][y] =1
    if k == 0 :
        for i in range(5) :
            if validation(x+i-2,y) :
                lst[x+i-2][y] = 1
    if k == 1 :
        if validation(x-1,y) :
            lst[x-1][y] = 1 
        if validation(x,y-1) :
            lst[x][y-1] =1 
        if validation(x+1,y) :
            lst[x+1][y] =1 
        if validation(x,y+1) :
            lst[x][y+1] =1 
    if k ==2 :
        if validation(x+1,y+1) :
            lst[x+1][y+1] = 1 
        if validation(x+1,y-1) :
            lst[x+1][y-1] =1 
        if validation(x-1,y+1) :
            lst[x-1][y+1] =1 
        if validation(x-1,y-1) :
            lst[x-1][y-1] =1 

            

bomPosLst =[]

for i in range(n) :
    for j in range(n) :
        if matrix[i][j] == 1 :
            bomPosLst.append((i,j))



maxCnt =0

def recursion(x,y) :
    global maxCnt
    if x == len(bomPosLst) :
        cnt =0
        permutation = tuple(map(int,y.split()))
        lst =[
            [0]*n
            for _ in range(n)
        ]
        for i in range(len(bomPosLst)) :
            explode(bomPosLst[i][0],bomPosLst[i][1],permutation[i],lst)

        for i in range(n) :
            for j in range(n) :
                if lst[i][j] == 1 :
                    cnt +=1
        
        maxCnt= max(maxCnt,cnt)


        return
    
    for i in range(3):
        recursion(x+1,y+" "+str(i) )



recursion(0,"")
print(maxCnt)