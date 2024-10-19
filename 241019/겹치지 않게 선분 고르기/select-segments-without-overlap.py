n = int(input())


line =[
    list(map(int,input().split()))
    for _ in range(n)
]
answer=0
def choose(index, maxNum,cnt) :
    global answer
    if index== n :
        answer = max(answer,cnt)
        return

    for i in range(index,n) :
        if maxNum < line[i][0] :
            maxNum = line[i][1]
            cnt +=1
        choose(i+1,maxNum,cnt)


choose(0,0,0)
print(answer)