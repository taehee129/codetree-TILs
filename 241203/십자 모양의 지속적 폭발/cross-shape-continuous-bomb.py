def valid(x,y,maxX,maxY) : 
    if (x<0 or x>=maxX) or (y<0 or y >=maxY) :
        return False
    return True

def explode(col, mat) : 
    
    n = len(mat)
    new = [
        lst[:] for lst in mat
    ]

    row = 0 

    for i in range(n) :
        row= i
        if mat[i][col] != 0 :
            break

    val = mat[row][col]

    #print(row,col,val)
    for i in range(col-val+1, col+val) :
        if not valid(row,i,n,n) :
            continue
        mat[row][i] = 0
        #print(row, i ,mat[row][i])
    for j in range(row-val+1, row+val) :
        if not valid(j,col,n,n) :
            continue
        mat[j][col] = 0
    

    return mat

def gravity(mat) : 

    n = len(mat)
    new = [
        [0 for _ in range(n)] for _ in range(n)
    ]
   

    for i in range(n) : 
        end = n-1
        for j in range(n-1,-1,-1) :   
            
            new[end][i] = mat[j][i]
            end -=1 

            if mat[j][i] == 0 :
                end +=1
    return new

            




n,m = tuple(map(int,input().split()))

mat = [
    list(map(int,input().split())) 
    for _ in range(n)
]

for _ in range(m) :
    col = int(input())
    col -=1
    mat = explode(col,mat)
    mat = gravity(mat)

for lst in mat :
    print(" ".join(map(str, lst)))
