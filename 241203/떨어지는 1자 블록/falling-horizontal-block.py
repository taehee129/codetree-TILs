
n,m,k = tuple(map(int,input().split()))

lst = [
    list(map(int,input().split()))
    for _ in range(n)
]

k-=1 

row = 0 

minRow = n-1

for i in range(k,k+m) :
    for j in range(n) :
        if lst[j][i] != 0 :
            minRow = min(minRow, j-1)
            break


for i in range(k,k+m) : 
    lst[minRow][i] = 1


for l in lst :
    print(" ".join(map(str,l)))


