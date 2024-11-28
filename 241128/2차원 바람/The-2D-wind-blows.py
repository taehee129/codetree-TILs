

def rangeFun(x,y,row,col) :
    if (x<0 or x>=row) or (y<0 or y>=col) :
        return False
    return True

def sumFun(x,y,mat) : 
    xd, yd = [1,0,-1,0],[0,-1,0,1] 
    a=0
    ret = 0
    for i in range(4) :
        temX,temY = x+xd[i], y+yd[i]
        if rangeFun(temX,temY,len(mat),len(mat[0])) :
            
            ret += mat[temX][temY]
            a+=1
    
    return ((ret+mat[x][y])//(a+1))

def rotate(x1,x2,y1,y2,matrix) :
    newMat= []
    for lst in matrix :
        newMat.append(lst[:])

    for i in range(y1+1,y2+1) :
        newMat[x1][i] = matrix[x1][i-1]

    for i in range(x1+1,x2+1) :
        newMat[i][y2] = matrix[i-1][y2]

    for i in range(y2-1,y1-1,-1) :
        newMat[x2][i] = matrix[x2][i+1]   

    for i in range(x2-1,x1-1,-1) :
        newMat[i][y1] = matrix[i+1][y1]    

    return newMat
       
n,m,q = tuple(map(int, input().split()))

matrix = [
    list(map(int,input().split())) 
    for _ in range(n)
]
    

for _ in range(q) :
    x1,y1,x2,y2 = tuple(map(lambda x : int(x)-1, input().split()))
    matrix = rotate(x1,x2,y1,y2,matrix)

    newMat= []
    for lst in matrix :
        newMat.append(lst[:])

    for i in range(x1,x2+1) :
        for j in range(y1,y2+1) :
            newMat[i][j] = sumFun(i,j,matrix)
    matrix = newMat
    

for row in range(n):
    for col in range(m):
        print(matrix[row][col], end = " ")
    print()