# 열과 행 모두 
# 수열의 수 출력 

n,m = tuple(map(int, input().split()))

mat =[]

for _ in range(n) : 
    mat.append(list(map(int, input().split())))


res =0
flag =False
for i in range(n) : 
    cnt=0
    num=0
    for j in range(n) : 
        if mat[i][j] == num : 
            cnt +=1
        else : 
            cnt =0 
        if cnt+1 >= m : 
            flag = True                
        num = mat[i][j]
    if flag == True : 
        res +=1 
    flag = False

for i in range(n) : 
    cnt=0
    num=0
    for j in range(n) : 
        if mat[j][i] == num : 
            cnt +=1 
        else : 
            cnt =0 
        if cnt+1 >= m :
            flag = True 
        num = mat[j][i]
    if flag : 
        res +=1
    flag = False
    
print(res)