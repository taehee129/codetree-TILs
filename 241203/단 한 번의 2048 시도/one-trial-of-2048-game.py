def gravityR(matrix) :

    newMatrix = []

    col = len(matrix)
    row = len(matrix[0])   

    isChange = False
    for i in range(col) :
        lst = [0 for _ in range(row)]
        end = row-1 
        for j in range(row-1,-1,-1) : 
            val =  matrix[i][j]
            if val ==0 :
                continue            

            if end != row-1 and val == lst[end+1] and isChange == False: 
                lst[end+1] += val 
                isChange = True 
                continue
            
            lst[end] = matrix[i][j]
            end -=1 
            isChange = False
     
        newMatrix.append(lst)

    return newMatrix

def gravityL(matrix) :

    newMatrix = []

    col = len(matrix)
    row = len(matrix[0])   

    isChange = False
    for i in range(col) :
        lst = [0 for _ in range(row)]
        end = 0 
        for j in range(row) : 
            val =  matrix[i][j]
            if val ==0 :
                continue            

            if end != 0 and val == lst[end-1] and isChange == False: 
                lst[end-1] += val 
                isChange = True 
                continue
            
            lst[end] = matrix[i][j]
            end +=1 
            isChange = False
     
        newMatrix.append(lst)

    return newMatrix

def gravityD(matrix) :
    col = len(matrix)
    row = len(matrix[0])   

    new = [[0 for _ in range(row)] for _ in range(col)]


    isChange = False
    for i in range(row) :

        end = col-1 
        for j in range(col-1,-1,-1) : 

            val =  matrix[j][i]
            if val ==0 :
                continue            

            if end != col-1 and val == new[end+1][i]and isChange == False: 
                new[end+1][i] += val 
                isChange = True 
                continue
            
            new[end][i] = val
            end -=1 
            isChange = False

    return new

def gravityU(matrix) :
    col = len(matrix)
    row = len(matrix[0])   

    new = [[0 for _ in range(row)] for _ in range(col)]


    isChange = False
    for i in range(row) :

        end = 0 
        for j in range(col) : 

            val =  matrix[j][i]
            if val ==0 :
                continue            

            if end != 0 and val == new[end-1][i]and isChange == False: 
                new[end-1][i] += val 
                isChange = True 
                continue
            
            new[end][i] = val
            end +=1 
            isChange = False

    return new


matrix = [
    list(map(int,input().split()))
    for _ in range(4)
]

d = input()

if d =="L" :
    matrix = gravityL(matrix)
elif d== "R" :
    matrix = gravityR(matrix)
elif d=="U" :
    matrix = gravityU(matrix)
else :
    matrix = gravityD(matrix)

for lst in matrix :
    print(" ".join(map(str,lst)))




