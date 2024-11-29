def valid(x,y,maxX,maxY) :
    if (x<0 or x>=maxX) or (y<0 or y>=maxY) :
        return False
    return True 

def explode(x,y,matrix) : 
    newMat = [
        list(lst) for lst in matrix
    ]

    bound = matrix[x][y]
    row = len(matrix)
    col = len(matrix[0])
    for i in range(x-bound+1,x+bound) :
        if valid(x,i,row,col) :
            newMat[i][y] = 0
            newMat = gravity(i,y,newMat)
        
        
    for i in range(y-bound+1,y+bound) :
        if i==y:
            continue
        if valid(x,i,row,col) :
            newMat = gravity(x,i,newMat)
    
    return newMat
    
def gravity(x,y,matrix) :
    newMat = [
        list(lst) for lst in matrix
    ]
    row = len(matrix)
    col = len(matrix[0])

    newMat[0][y] = 0
    for i in range(x,0,-1) :
        newMat[i][y] = matrix[i-1][y]
    
    return newMat

n = int(input())

matrix = [
    list(map(int,input().split()))
    for _ in range(n)
]

x,y = tuple(map(int, input().split()))

matrix = explode(x-1,y-1,matrix)

for lst in matrix :
    print(" ".join(map(str,lst)))