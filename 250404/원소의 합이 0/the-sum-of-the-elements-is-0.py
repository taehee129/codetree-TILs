n = int(input())

seqs = [list(map(int,input().split())) for _ in range(4)]


d = {}

for i in range(n) : 
    val =  seqs[0][i]
    if val in d :
        d[val] +=1 
    else :
        d[val] = 1
cnt =0

for i in range(n) :
    for j in range(n) :
        for k in range(n) :
            val = -(seqs[1][i] + seqs[2][j] + seqs[3][k])
            if val in d :
                cnt += d[val]

print(cnt)
